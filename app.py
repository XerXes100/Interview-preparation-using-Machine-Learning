import os
from flask import Flask, render_template, request, url_for, redirect, session, flash
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

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQLShell@900",  # Change password according to system
    database="interview_preparation",
)

# Define the upload folder where the audio files will be saved
app.config["recordings"] = "uploads/"

# Set a secret key for Flask's session management
app.secret_key = "abc123"

cursor = mydb.cursor()
transcript = ""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("reached post method")
        email = request.form.get("email")
        password = request.form.get("password")

        user_data = database.fetch_entry(email=email, password=password)
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

        value_check = database.user_entry(
            username=username, email=email, password=password
        )

        if value_check == "Value inserted":
            return render_template("home.html", username=username)
        else:
            return render_template("signup.html", result="Account already exists!")
    else:
        return render_template("signup.html")


@app.route("/home")
def home():
    # cursor.execute("Select * from users where emailID = %s", ("emailID"))
    # userDetails = cursor.fetchall()
    return render_template("home.html")


@app.route("/practice")
def practice():
    return render_template("practice.html")


@app.route("/record/<int:questionID>", methods=["GET", "POST"])
def recordQuestion(questionID):
    if request.method == "POST" and request.form.get("Record") == "Record":
        global transcript
        r = sr1.Recognizer()

        samplerate = 44100  # Hertz
        duration = 10  # seconds
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
        s, t = speech_text.save_transcript(
            audio_url, "file_title", sentiment_analysis=True
        )
        print(s)
        transcript = s
        print(nlp.entity_analysis_q1(s))
        print("confidence analysis:", t)
        return render_template("practice_ques.html", transcript=s)
    elif (
        request.method == "POST"
        and request.form.get("Submit_Answer") == "Submit_Answer"
    ):
        now = datetime.now()

        current_date = now.date()
        current_time = now.time()
        database.add_response(questionID, transcript, current_date, current_time)

        return render_template("practice.html")
    else:
        return render_template("practice_ques.html")


@app.route("/review")
def review():
    database.fetch_current_user_responses()
    return render_template("review.html")


# @app.route("/profile")
def profile():
    cursor.execute("Select * from users where emailID = %s", ("emailID"))
    userDetails = cursor.fetchall()
    print(userDetails)


@app.route("/feedback")
def feedback():
    g = open("user.json")
    data = json.load(g)
    return render_template("feedback.html", username=data["username"])


@app.route("/logout")
def logout():
    cursor.execute("select * from users where email = %s", [])

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
