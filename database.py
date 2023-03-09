import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQLShell@900",  # Change password according to system
    database="interview_preparation",
)

cursor = mydb.cursor()


def create_table():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users ( \
            userID INT PRIMARY KEY, \
            username VARCHAR (255), \
            email VARCHAR(255), \
            password VARCHAR(255), \
            photo LONGBLOB NOT NULL, \
            isLoggedIn BOOL \
        );"
    )
    # "CREATE TABLE IF NOT EXISTS movie_details(movie_id INT primary key,movie_name VARCHAR(20), genre VARCHAR(20), rating FLOAT, movie_release_date DATE,movie_duration VARCHAR(20),movie_description VARCHAR(500))")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS questions ( \
            questionID INT PRIMARY KEY, \
            question VARCHAR(1000), \
            ideal_answer VARCHAR(3000) \
        );"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS responses ( \
            responseID INT PRIMARY KEY, \
            userID INT, \
            questionID INT, \
            response_text VARCHAR(1000), \
            response_audio BLOB, \
            feedback VARCHAR(1000), \
            date DATE, \
            time TIME, \
            CONSTRAINT fk1 FOREIGN KEY (userID) REFERENCES users(userID) ON UPDATE CASCADE ON DELETE CASCADE, \
            CONSTRAINT fk2 FOREIGN KEY (questionID) REFERENCES questions(questionID) ON UPDATE CASCADE ON DELETE CASCADE \
        );"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS output ( \
            outputID INT PRIMARY KEY, \
            responseID INT, \
            confidence FLOAT, \
            positive_sentiment FLOAT, \
            negative_sentiment FLOAT, \
            neutral_sentiment FLOAT, \
            frequency FLOAT, \
            pitch FLOAT, \
            intensity FLOAT, \
            CONSTRAINT fk FOREIGN KEY (responseID) REFERENCES responses(responseID) ON UPDATE CASCADE ON DELETE CASCADE \
        )"
    )

    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS customer(email_id VARCHAR(20) primary key,name VARCHAR(20),password VARCHAR(20), phone INT(10), age INT)")
    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS record(tickets_booked INT,seat_type VARCHAR(20),email_id VARCHAR(20),movie_id INT,show_date DATE, CONSTRAINT fk2 FOREIGN KEY(email_id)REFERENCES customer(email_id)ON UPDATE CASCADE ON DELETE CASCADE,CONSTRAINT fk3 FOREIGN KEY(movie_id)REFERENCES movie_details(movie_id)ON UPDATE CASCADE ON DELETE CASCADE,CONSTRAINT fk4 FOREIGN KEY(show_date)REFERENCES booking(show_date)ON UPDATE CASCADE ON DELETE CASCADE)")
    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS upcoming_movie(movie_name VARCHAR(20), genre VARCHAR(20), movie_ID INT primary key, movie_release_date DATE)")


def entries():
    sql_insert_user = "INSERT INTO users(userID, username, email, password, photo, isLoggedIn) VALUES(%s,%s,%s,%s,%s,%s)"
    with open("static/images/Feedback.png", "rb") as f:
        image_binary1 = f.read()
        
    with open("static/images/Future.png", "rb") as f:
        image_binary2 = f.read()

    user_vals = [
        (
            1,
            "Tirth Jain",
            "tirthjain1411@gmail.com",
            "abc123",
            image_binary1,
            True
        ),
        (
            2,
            "L Sangrith Krishna",
            "lsangrith@gmail.com",
            "abc1234",
            image_binary2,
            False
        ),
    ]
    cursor.executemany(sql_insert_user, user_vals)
    # cursor.execute
    mydb.commit()
    print(cursor.rowcount, "were inserted")

    # sql_insert_booking = "INSERT INTO booking(movie_id,show_date,tickets_remaining,price,seat_type) VALUES(%s,%s,%s,%s,%s)"
    # booking_vals = [
    #     (100, "2021-04-10", 30, 150, "Silver"),
    #     (100, "2021-04-10", 20, 200, "Gold"),
    #     (101, "2021-04-10", 30, 150, "Silver"),
    #     (101, "2021-04-10", 20, 200, "Gold"),
    #     (102, "2021-04-10", 30, 160, "Silver"),
    #     (102, "2021-04-10", 20, 200, "Gold"),
    #     (103, "2021-04-10", 30, 160, "Silver"),
    #     (103, "2021-04-10", 20, 220, "Gold"),
    #     (104, "2021-04-10", 30, 180, "Silver"),
    #     (104, "2021-04-10", 20, 220, "Gold"),
    #     (105, "2021-04-10", 30, 180, "Silver"),
    #     (105, "2021-04-10", 20, 230, "Gold"),
    #     (100, "2021-04-11", 30, 170, "Silver"),
    #     (100, "2021-04-11", 20, 250, "Gold"),
    #     (101, "2021-04-11", 30, 170, "Silver"),
    #     (101, "2021-04-11", 20, 250, "Gold"),
    #     (102, "2021-04-11", 30, 180, "Silver"),
    #     (102, "2021-04-11", 20, 250, "Gold"),
    #     (103, "2021-04-11", 30, 180, "Silver"),
    #     (103, "2021-04-11", 20, 260, "Gold"),
    #     (104, "2021-04-11", 30, 190, "Silver"),
    #     (104, "2021-04-11", 20, 260, "Gold"),
    #     (105, "2021-04-11", 30, 190, "Silver"),
    #     (105, "2021-04-11", 20, 270, "Gold"),
    #     (100, "2021-04-12", 30, 170, "Silver"),
    #     (100, "2021-04-12", 20, 250, "Gold"),
    #     (101, "2021-04-12", 30, 170, "Silver"),
    #     (101, "2021-04-12", 20, 250, "Gold"),
    #     (102, "2021-04-12", 30, 180, "Silver"),
    #     (102, "2021-04-12", 20, 250, "Gold"),
    #     (103, "2021-04-12", 30, 180, "Silver"),
    #     (103, "2021-04-12", 20, 260, "Gold"),
    #     (104, "2021-04-12", 30, 190, "Silver"),
    #     (104, "2021-04-12", 20, 260, "Gold"),
    #     (105, "2021-04-12", 30, 190, "Silver"),
    #     (105, "2021-04-12", 20, 270, "Gold"),
    # ]
    # cursor.executemany(sql_insert_booking, booking_vals)
    # mydb.commit()
    # print(cursor.rowcount, "were inserted")


create_table()
entries()
