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
            photo BLOB, \
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
    sql_insert_movie = "INSERT INTO users(userID, username, email, password,rating,movie_release_date,movie_duration,movie_description) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    movie_vals = [
        (
            100,
            "Avengers Endgame",
            "Sci-Fi",
            4.5,
            "2021-04-09",
            180,
            "The fourth installment in the Avengers saga is the culmination of 22 interconnected films and the climax of an epic journey. Earth’s heroes will finally understand how fragile our reality is—and the sacrifices that must be made to uphold it—in a story of friendship, teamwork and setting aside differences to overcome an impossible obstacle.",
        ),
        (
            101,
            "Bohemian Rhapsody",
            "Drama",
            4,
            "2021-04-09",
            133,
            "Bohemian Rhapsody is an enthralling celebration of Queen, their music, and their extraordinary lead singer Freddie Mercury, who defied stereotypes and convention to become one of history’s most beloved entertainers. Following Queen’s meteoric rise, their revolutionary sound and Freddie’s solo career, the film also chronicles the band’s reunion, and one of the greatest performances in rock history.",
        ),
        (
            102,
            "1917",
            "Action",
            4,
            "2021-04-09",
            119,
            "When the British army receives vital intel about German battle plans, two British corporals are sent across enemy lines in a race to deliver the message in time and prevent 1,600 men from blindly walking into an attack.",
        ),
        (
            103,
            "Jojo Rabbit",
            "Comedy",
            4.5,
            "2021-04-02",
            108,
            "Hitler Youth cadet Jojo Betzler firmly believes in the ideals of Nazism manifested by his imaginary friend, Adolf Hitler. However, his foundations are shaken when he finds a Jewish girl in his house.",
        ),
        (
            104,
            "Joker",
            "Thriller",
            3.5,
            "2021-04-02",
            122,
            "Joker centers around the iconic arch-nemesis and is an original, standalone story not seen before on the big screen. The exploration of Arthur Fleck (Joaquin Phoenix), a man disregarded by society, is not only a gritty character study, but also a broader cautionary tale.",
        ),
        (
            105,
            "Ford vs Ferrari",
            "Action",
            4,
            "2021-04-02",
            152,
            "American automotive designer Carroll Shelby and fearless British race car driver Ken Miles battle corporate interference, the laws of physics and their own personal demons to build a revolutionary vehicle for the Ford Motor Co. Together, they plan to compete against the race cars of Enzo Ferrari at the 24 Hours of Le Mans in France in 1966.",
        ),
    ]
    cursor.executemany(sql_insert_movie, movie_vals)
    mydb.commit()
    print(cursor.rowcount, "were inserted")

    sql_insert_booking = "INSERT INTO booking(movie_id,show_date,tickets_remaining,price,seat_type) VALUES(%s,%s,%s,%s,%s)"
    booking_vals = [
        (100, "2021-04-10", 30, 150, "Silver"),
        (100, "2021-04-10", 20, 200, "Gold"),
        (101, "2021-04-10", 30, 150, "Silver"),
        (101, "2021-04-10", 20, 200, "Gold"),
        (102, "2021-04-10", 30, 160, "Silver"),
        (102, "2021-04-10", 20, 200, "Gold"),
        (103, "2021-04-10", 30, 160, "Silver"),
        (103, "2021-04-10", 20, 220, "Gold"),
        (104, "2021-04-10", 30, 180, "Silver"),
        (104, "2021-04-10", 20, 220, "Gold"),
        (105, "2021-04-10", 30, 180, "Silver"),
        (105, "2021-04-10", 20, 230, "Gold"),
        (100, "2021-04-11", 30, 170, "Silver"),
        (100, "2021-04-11", 20, 250, "Gold"),
        (101, "2021-04-11", 30, 170, "Silver"),
        (101, "2021-04-11", 20, 250, "Gold"),
        (102, "2021-04-11", 30, 180, "Silver"),
        (102, "2021-04-11", 20, 250, "Gold"),
        (103, "2021-04-11", 30, 180, "Silver"),
        (103, "2021-04-11", 20, 260, "Gold"),
        (104, "2021-04-11", 30, 190, "Silver"),
        (104, "2021-04-11", 20, 260, "Gold"),
        (105, "2021-04-11", 30, 190, "Silver"),
        (105, "2021-04-11", 20, 270, "Gold"),
        (100, "2021-04-12", 30, 170, "Silver"),
        (100, "2021-04-12", 20, 250, "Gold"),
        (101, "2021-04-12", 30, 170, "Silver"),
        (101, "2021-04-12", 20, 250, "Gold"),
        (102, "2021-04-12", 30, 180, "Silver"),
        (102, "2021-04-12", 20, 250, "Gold"),
        (103, "2021-04-12", 30, 180, "Silver"),
        (103, "2021-04-12", 20, 260, "Gold"),
        (104, "2021-04-12", 30, 190, "Silver"),
        (104, "2021-04-12", 20, 260, "Gold"),
        (105, "2021-04-12", 30, 190, "Silver"),
        (105, "2021-04-12", 20, 270, "Gold"),
    ]
    cursor.executemany(sql_insert_booking, booking_vals)
    mydb.commit()
    print(cursor.rowcount, "were inserted")


create_table()
# entries()
