from flask import Flask, render_template, request, url_for, redirect, session
import re
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQLShell@900",  # Change password according to system
    database="interview_preparation",
)

cursor = mydb.cursor()

# app.secret_key = 'hello123'

# movie_image=["static/resources/endgame_rect.jpg","static/resources/br_rect.jpg","static/resources/1917_rect.jpg","static/resources/jojo_rect.jpg","static/resources/joker_rect.jpg","static/resources/fvf_rect.jpg"]


@app.route("/")

# @app.route("/filmsy")
# @app.route("/home")
def index():
    return render_template("home.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/home")
def home():
    cursor.execute("Select * from users where emailID = %s", ("emailID"))
    userDetails = cursor.fetchall()
    return render_template("home.html")

@app.route("/practice")
def practice():
    return render_template("practice.html")


@app.route("/review")
def review():
    return render_template("review.html")

# @app.route("/profile")
def profile():
    cursor.execute("Select * from users where emailID = %s", ("emailID"))
    userDetails = cursor.fetchall()

    print(userDetails)
    # isUserLoggedIn = userDetails[0]['isLoggedIn']
    # if "loggedin" in session:
    #     cursor.execute("Select * from users where email_id= %s", (session["emailID"],))
    #     record = cursor.fetchall()
    #     movie = []
    #     genre = []
    #     l = len(record)
    #     for i in range(len(record)):
    #         cursor.execute(
    #             "Select movie_name from movie_details where movie_id=%s",
    #             (record[i][3],),
    #         )
    #         movie.append(cursor.fetchone())
    #         cursor.execute(
    #             "Select genre from movie_details where movie_id=%s", (record[i][3],)
    #         )
    #         genre.append(cursor.fetchone())
    #     return render_template(
    #         "profile.html",
    #         account=session,
    #         record=record,
    #         movie=movie,
    #         genre=genre,
    #         len=l,
    #     )
    # else:
    #     return render_template("login.html")


# # @app.route("/book", methods=["GET", "POST"])
# def book():
#     if request.method == "POST":
#         if "loggedin" in session:
#             if request.form["movie"] == "selected":
#                 try:
#                     id = request.form["bt"]
#                     date = request.form["date"]
#                     cursor.execute(
#                         "Select * from movie_details where movie_id=%s", (id,)
#                     )
#                     movie = cursor.fetchone()
#                     cursor.execute(
#                         "Select tickets_remaining from booking where show_date=%s and movie_id=%s and seat_type='Gold'",
#                         (date, id),
#                     )
#                     goldtic = cursor.fetchone()
#                     cursor.execute(
#                         "Select tickets_remaining from booking where show_date=%s and movie_id=%s and seat_type='Silver'",
#                         (date, id),
#                     )
#                     silvertic = cursor.fetchone()
#                     id = int(id)
#                     recommend = mini_project.genre_recommendations(movie[1])
#                     return render_template(
#                         "bookings.html",
#                         img=movie_image[id - 100],
#                         movie=movie,
#                         goldtic=int(goldtic[0]),
#                         silvertic=int(silvertic[0]),
#                         recommend=recommend,
#                         date=date,
#                     )
#                 except:
#                     return render_template("index.html")
#         else:
#             return render_template("login.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     msg = ""
#     if (
#         request.method == "POST"
#         and "email" in request.form
#         and "password" in request.form
#     ):
#         username = request.form["email"]
#         password = request.form["password"]
#         cursor.execute(
#             "SELECT * FROM customer WHERE email_id = %s AND password = %s",
#             (username, password),
#         )
#         account = cursor.fetchone()
#         if account:  # session is inbuilt
#             session["loggedin"] = True
#             session["name"] = account[1]
#             session["username"] = account[0]
#             session["phone"] = account[3]
#             return render_template("index.html")
#         else:
#             msg = "Incorrect username/password!"
#     return render_template("login.html", msg=msg)


# @app.route("/register", methods=["POST", "GET"])
# def register():
#     msg = ""
#     # Check if "username", "password" and "email" POST requests exist (user submitted form)
#     if (
#         request.method == "POST"
#         and "name" in request.form
#         and "password" in request.form
#         and "email" in request.form
#         and "age" in request.form
#         and "phone" in request.form
#     ):
#         # Create variables for easy access
#         username = request.form["email"]
#         password = request.form["password"]
#         name = request.form["name"]
#         age = request.form["age"]
#         phone = request.form["phone"]
#         cursor.execute(
#             "SELECT * FROM customer WHERE email_id = %s", (username,)
#         )  # should be a tuple
#         account = cursor.fetchone()
#         # If account exists show error and validation checks
#         if account:
#             msg = "Account already exists!"
#         elif not re.match(r"[^@]+@[^@]+\.[^@$%]+", username):
#             msg = "Invalid email address!"
#         elif not re.match(r"[A-Za-z0-9]+", name):
#             msg = "Username must contain only characters and numbers!"
#         elif len(phone) != 9:
#             msg = "Please enter 9 digit phone number"
#         elif not username or not password or not name:
#             msg = "Please fill out the form!"
#         else:
#             age = int(age)
#             phone = int(phone)
#             # Account doesnt exists and the form data is valid, now insert new account into accounts table
#             cursor.execute(
#                 "INSERT INTO customer VALUES (%s, %s, %s,%s,%s)",
#                 (username, name, password, phone, age),
#             )
#             mydb.commit()
#             return render_template("index.html")
#     elif request.method == "POST":
#         # Form is empty... (no POST data)
#         msg = "Please fill out the form!"
#     # Show registration form with message (if any)
#     return render_template("login.html", msg=msg)


# @app.route("/payment", methods=["GET", "POST"])
# def payment():
#     if request.method == "POST":
#         tickettype = request.form["ticket-type"]
#         movieint = request.form["animal"]
#         booked = request.form["quantity"]
#         dateint = request.form["whatdate"]
#         cursor.execute(
#             "Select movie_name from movie_details where movie_id=%s", (movieint,)
#         )
#         moviename = cursor.fetchone()
#         cursor.execute(
#             "Select price from booking where show_date=%s and movie_id=%s and seat_type=%s",
#             (dateint, movieint, tickettype),
#         )
#         price = cursor.fetchone()
#         total = int(price[0]) * int(booked)
#         cursor.execute(
#             "Select tickets_remaining from booking where show_date=%s and movie_id=%s and seat_type=%s",
#             (dateint, movieint, tickettype),
#         )
#         left = cursor.fetchone()
#         left = int(int(left[0]) - int(booked))
#         email = session["username"]
#         cursor.execute(
#             "Update booking set tickets_remaining= %s where show_date=%s and movie_id=%s and seat_type=%s",
#             (left, dateint, int(movieint), tickettype),
#         )
#         cursor.execute(
#             "Select * from record where email_id=%s and movie_id=%s and show_date=%s and seat_type=%s",
#             (email, int(movieint), dateint, tickettype),
#         )
#         prevrecord = cursor.fetchone()
#         if prevrecord:
#             booked = int(int(booked) + int(prevrecord[0]))
#             cursor.execute(
#                 "Update record set tickets_booked=%s where email_id=%s and movie_id=%s and show_date=%s and seat_type=%s",
#                 (booked, email, int(movieint), dateint, tickettype),
#             )
#         else:
#             cursor.execute(
#                 "INSERT INTO record VALUES (%s, %s, %s, %s, %s)",
#                 (int(booked), tickettype, email, int(movieint), dateint),
#             )
#         mydb.commit()
#         return render_template(
#             "payment.html",
#             moviename=moviename[0],
#             dateint=dateint,
#             tickettype=tickettype,
#             booked=booked,
#             price=price[0],
#             total=total,
#         )


# @app.route("/pythonlogin/logout", methods=["POST", "GET"])
# def logout():
#     # Remove session data, this will log the user out
#     session.pop("loggedin", None)
#     session.pop("id", None)
#     session.pop("username", None)
#     # Redirect to login page
#     return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
    profile()
