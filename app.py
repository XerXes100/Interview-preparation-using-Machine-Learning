import os
from flask import Flask, render_template, request, url_for, redirect, session, flash
import re
import mysql.connector
from flask import request
import database
from werkzeug.utils import secure_filename

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQLShell@900",  # Change password according to system
    database="interview_preparation",
)

# Define the upload folder where the audio files will be saved
app.config['recordings'] = 'uploads/'

# Set a secret key for Flask's session management
app.secret_key = 'abc123'

cursor = mydb.cursor()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("reached post method")
        email = request.form.get("email")
        password = request.form.get("password")
        
        username_fetched = database.fetch_entry(email=email, password=password)
        print(username_fetched)
        return render_template('home.html', username=username_fetched)
    else:
        return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        value_check = database.user_entry(username=username, email=email, password=password)
        
        if value_check == "Value inserted":
            return render_template('home.html', username=username)
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

@app.route("/record", methods=['GET', 'POST'])
def record():
    if request.method == 'POST':
        if 'audio_data' not in request.files:
            flash('No file part')
            return render_template('practice.html')
        file = request.files['audio_data']
        # Check if a file was selected
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # Generate a secure filename and save the uploaded file to the upload folder
        filename = secure_filename(file.filename if file.filename else 'default_audio.wav')
        file.save(os.path.join(app.config['recordings'], filename))
        # Display a message indicating the file was uploaded successfully
        flash('File uploaded successfully')
        return render_template("practice.html")
    else:
        return render_template("record_audio.html")

@app.route("/review")
def review():
    return render_template("review.html")

# @app.route("/profile")
def profile():
    cursor.execute("Select * from users where emailID = %s", ("emailID"))
    userDetails = cursor.fetchall()
    print(userDetails)

@app.route("/logout")
def logout():
    cursor.execute("select * from users where email = %s", [])
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
    # profile()
