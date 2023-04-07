import os
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    session,
    flash,
    send_file,
)
import re
import mysql.connector
from flask import request
import database
from werkzeug.utils import secure_filename
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr1
import nlp
import json
from datetime import datetime
import speech_text, feedback_analysis
from markupsafe import Markup

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sang123",  # Change password according to system
    database="interview_preparation",
)

# Define the upload folder where the audio files will be saved
app.config["recordings"] = "uploads/"

# Set a secret key for Flask's session management
app.secret_key = "abc123"

cursor = mydb.cursor()
transcript = ""
sentiment_analysis = {}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("reached post method")
        email = request.form.get("email")
        password = request.form.get("password")

        user_data = database.fetch_current_user(email=email, password=password)
        print(user_data)
        json_object = json.dumps(user_data, indent=5)
        with open("user.json", "w") as outfile:
            outfile.write(json_object)
        return render_template("home.html", username=user_data["username"])
    else:
        return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        value_check = database.insert_user(
            username=username, email=email, password=password
        )

        if value_check == "Value inserted":
            user_data = database.fetch_current_user(email=email, password=password)
            print(user_data)
            json_object = json.dumps(user_data, indent=5)
            with open("user.json", "w") as outfile:
                outfile.write(json_object)
            return render_template("home.html", username=username)
        else:
            return render_template("signup.html", result="Account already exists!")
    else:
        return render_template("signup.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/practice")
def practice():
    return render_template("practice.html")


@app.route("/record/<int:questionID>", methods=["GET", "POST"])
def recordQuestion(questionID):
    if request.method == "POST" and request.form.get("Record") == "Record":
        global transcript
        global sentiment_analysis
        r = sr1.Recognizer()

        samplerate = 44100  # Hertz
        duration = 35  # seconds
        filename = "output.wav"

        print("\n")
        print("Start talking:")
        # mydata = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, blocking=True)
        # sf.write(filename, mydata, samplerate)
        hellow = sr1.AudioFile("output.wav")
        with hellow as source:
            audio = r.record(source)
        import speech_text

        audio_url = speech_text.upload(filename)
        t, s = speech_text.save_transcript(
            audio_url, "file_title", sentiment_analysis=True
        )
        transcript = t
        sentiment_analysis = s
        print(nlp.entity_analysis_q1(t))
        print("confidence analysis:", s)
        return render_template("practice_ques.html", transcript=t)
    elif (
        request.method == "POST"
        and request.form.get("Submit_Answer") == "Submit_Answer"
    ):
        now = datetime.now()

        current_date = now.date()
        current_time = now.time()

        responseID = database.add_response(
            questionID, transcript, current_date, current_time, sentiment_analysis
        )

        feedbackAnalysisData = database.insert_output(
            responseID, transcript, questionID, sentiment_analysis
        )

        # print(feedbackAnalysisData)
        json_object = json.dumps(feedbackAnalysisData)
        with open("feedbackAnalysis.json", "w") as outfile:
            outfile.write(json_object)

        return render_template("practice.html")
    else:
        return render_template("practice_ques.html", questionID=questionID)


@app.route("/review")
def review():
    database.fetch_current_user_responses()
    f = open("responses.json")
    data = json.load(f)
    return render_template("review.html", responses=data)


@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


@app.route("/feedbackData/<getResponseFromJson>")
def feedbackData(getResponseFromJson):
    global sentiment_analysis

    g = open("user.json")
    userData = json.load(g)

    h = open("questions.json")
    questionData = json.load(h)

    k = open("responses.json")
    responseData = json.load(k)

    l = open("feedbackAnalysis.json")
    feedbackAnalysisData = json.load(l)

    # print(questionData)
    # print(getResponseFromJson)
    # print(responseData[getResponseFromJson])

    new_response_json_string = responseData[getResponseFromJson]

    print(new_response_json_string["questionID"])

    str1 = ""
    with open("static/feedbackImages/sentence.svg") as file:
        for item in file:
            str1 += item
            # print(item)

    userResponseFeedback = {
        "username": userData["username"],
        "question": questionData[str(new_response_json_string["questionID"])],
        "responseText": new_response_json_string["response_text"],
        "feedback": new_response_json_string["feedback"],
        "date": new_response_json_string["date"],
        "time": new_response_json_string["time"],
        "svg_element": str1,
        "sentimentText": feedbackAnalysisData["sentimentText"],
        "entityText": feedbackAnalysisData["entityText"],
        "missEntityText": feedbackAnalysisData["missEntityText"],
        "paceResultText": feedbackAnalysisData["paceResultText"],
    }

    return render_template("feedback.html", responseData=userResponseFeedback)


# @app.route("/sentence_analysis_image")
# def sentence_analysis_image():
#     filename = "static/feedbackImages/sentence.svg"
#     return send_file(filename, mimetype="image/svg+xml")


@app.route("/logout")
def logout():
    # cursor.execute("select * from users where email = %s", [])

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
