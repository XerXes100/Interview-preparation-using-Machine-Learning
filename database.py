import mysql.connector
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQLShell@900",  # Change password according to system
    database="interview_preparation",
)

cursor = mydb.cursor()


with open("static/images/Feedback.png", "rb") as f:
    image_binary1 = f.read()

with open("static/images/Future.png", "rb") as f:
    image_binary2 = f.read()


def create_table_users():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users ( \
            userID INT PRIMARY KEY, \
            username VARCHAR (255), \
            email VARCHAR(255), \
            password VARCHAR(255), \
            isLoggedIn BOOL \
        );"
    )


def create_table_questions():
    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS users ( \
    #         userID INT PRIMARY KEY, \
    #         username VARCHAR (255), \
    #         email VARCHAR(255), \
    #         password VARCHAR(255), \
    #         photo LONGBLOB NOT NULL, \
    #         isLoggedIn BOOL \
    #     );"
    # )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS questions ( \
            questionID INT PRIMARY KEY, \
            question VARCHAR(1000), \
            ideal_answer VARCHAR(3000) \
        );"
    )


def create_table_responses():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS responses ( \
            responseID INT PRIMARY KEY, \
            userID INT, \
            questionID INT, \
            response_text VARCHAR(1000), \
            feedback VARCHAR(1000), \
            date DATE, \
            time TIME, \
            CONSTRAINT fk1 FOREIGN KEY (userID) REFERENCES users(userID) ON UPDATE CASCADE ON DELETE CASCADE, \
            CONSTRAINT fk2 FOREIGN KEY (questionID) REFERENCES questions(questionID) ON UPDATE CASCADE ON DELETE CASCADE \
        );"
    )


def create_table_outputs():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS outputs ( \
            outputID INT PRIMARY KEY, \
            responseID INT, \
            questionID INT, \
            positive_sentiment INT, \
            negative_sentiment INT, \
            neutral_sentiment INT, \
            CONSTRAINT fk FOREIGN KEY (responseID) REFERENCES responses(responseID) ON UPDATE CASCADE ON DELETE CASCADE \
        )"
    )


def entries():
    sql_insert_user = "INSERT INTO users(userID, username, email, password, isLoggedIn) VALUES(%s,%s,%s,%s,%s)"

    user_vals = [
        (1, "Tirth Jain", "tirthjain1411@gmail.com", "abc123", image_binary1, True),
        (
            2,
            "L Sangrith Krishna",
            "lsangrith@gmail.com",
            "abc1234",
            image_binary2,
            False,
        ),
    ]
    cursor.executemany(sql_insert_user, user_vals)
    # cursor.execute
    mydb.commit()
    print(cursor.rowcount, "were inserted")


def add_questions():
    sql_insert_questions = (
        "INSERT INTO questions(questionID, question, ideal_answer) VALUES(%s,%s,%s)"
    )
    qvalues = [
        (
            1,
            "Tell me about yourself",
            "My name is Jane Smith, and I am a final year engineering student at Duke University, majoring in Electrical Engineering. I have a strong passion for developing innovative solutions to real-world problems through my studies in engineering. I have completed various projects and internships in the field of power systems, renewable energy, and control systems. I have a strong interest in the field of machine learning and have taken relevant courses to further my knowledge in this area. I am a highly motivated individual who is always eager to take on new challenges and expand my skill set. I aim to work in a research and development role where I can continue to learn and innovate in the field of engineering. Outside of my studies, I am an active member of the robotics club, where I have been a team lead for the past two years.",
        ),
        (2, "What are your strengths?", "xxx"),
        (
            3,
            "Where do you see yourself in the future?",
            "I am passionate about using my skills in technology to make a positive impact on society, and I see myself continuing to work in this field in the future. As the industry evolves, I plan to keep up with the latest developments and continue learning new technologies. Ultimately, I hope to become a respected leader in the field, mentoring and guiding others to develop innovative solutions to important problems",
        ),
    ]
    cursor.executemany(sql_insert_questions, qvalues)
    mydb.commit()


def fetch_users():
    cursor.execute("select * from users")
    userRecords = cursor.fetchall()
    for i in range(len(userRecords)):
        print(userRecords[i])


def insert_user(username, email, password):
    cursor = mydb.cursor(buffered=True)
    cursor.execute("select * from users where email = %s", [email])

    if cursor.rowcount == 0:
        cursor.execute("select * from users order by userID DESC LIMIT 1")
        last_user = cursor.fetchall()

        user_id = 1

        for row in last_user:
            last_user_id = row[0]
            user_id = int(str(last_user_id)) + 1

        loginValue = True

        sql_insert_user = f"INSERT INTO users(userID, username, email, password, isLoggedIn) VALUES \
            (%s, %s, %s, %s, %s);"

        values = [user_id, username, email, password, loginValue]

        cursor.execute(sql_insert_user, values)

        mydb.commit()
        return "Value inserted"
    else:
        return "Value exists"


def fetch_current_user(email, password):
    fetch_user = f"SELECT * FROM users WHERE email = %s and password = %s;"
    fetch_values = [email, password]
    cursor.execute(fetch_user, fetch_values)
    userRecords = cursor.fetchall()

    print(userRecords)

    if len(userRecords) == 1:
        (
            userID_fetched,
            username_fetched,
            email_fetched,
            password_fetched,
            isLoggedIn,
        ) = userRecords[0]
        return {
            "userID": userID_fetched,
            "username": username_fetched,
            "email": email_fetched,
            "password": password_fetched,
            "isLoggedIn": isLoggedIn,
        }
    else:
        return {
            "userID": "",
            "username": "",
            "email": "",
            "password": "",
            "isLoggedIn": "",
        }


def add_response(questionID, response, current_date, current_time, sentiment_analysis):
    f = open("user.json")
    data = json.load(f)
    f.close()

    feedback_text = "Kuch bi bai"

    cursor.execute("select * from responses order by responseID DESC LIMIT 1")
    last_response = cursor.fetchall()

    response_id = 1

    for row in last_response:
        last_response_id = row[0]
        response_id = int(str(last_response_id)) + 1

    # with open(filename, 'rb') as file:
    #     binary_data = file.read()

    # return binary_data

    # with open("output.wav", 'rb') as file:
    #     binaryData = file.read()

    sql_insert_response = f"INSERT INTO responses(\
        responseID, \
        userID, \
        questionID, \
        response_text, \
        feedback, \
        date, \
        time \
        ) VALUES (%s, %s, %s, %s, %s, %s, %s);"

    response_values = [
        response_id,
        data["userID"],
        questionID,
        response,
        feedback_text,
        current_date,
        current_time,
    ]

    cursor.execute(sql_insert_response, response_values)

    mydb.commit()

    insert_output(response_id, questionID, sentiment_analysis)
    fetch_current_user_responses()
    print("Response added successfully")


def insert_output(responseID, questionID, sentiment_analysis):
    pos, neu, neg = 0, 0, 0
    for i in sentiment_analysis:
        if i["sentiment"] == "POSITIVE":
            pos += 1
        elif i["sentiment"] == "NEUTRAL":
            neu += 1
        else:
            neg += 1

    print(pos, neu, neg)

    cursor.execute("select * from outputs order by outputID DESC LIMIT 1")
    last_output = cursor.fetchall()

    output_id = 1

    for row in last_output:
        last_output_id = row[0]
        output_id = int(str(last_output_id)) + 1

    sql_insert_output = f"INSERT INTO outputs(\
        outputID, \
        responseID, \
        questionID, \
        positive_sentiment, \
        negative_sentiment, \
        neutral_sentiment, \
        ) VALUES (%s, %s, %s, %s, %s, %s);"

    output_values = [output_id, int(responseID), int(questionID), pos, neg, neu]

    cursor.execute(sql_insert_output, output_values)

    mydb.commit()
    print("Output added successfully")


def fetch_responses():
    cursor.execute("select * from responses")
    userRecords = cursor.fetchall()
    for i in range(len(userRecords)):
        print(userRecords[i])


def fetch_current_user_responses():
    g = open("user.json")
    data = json.load(g)

    # with open('responses.json') as json_file:
    #     json_decoded = json.load(json_file)

    new_json = {}
    print(data["userID"])
    sql_fetch_query = (
        "select * from responses where userID = "
        + str(data["userID"])
        + " order by date desc, time desc;"
    )
    cursor.execute(sql_fetch_query)
    userRecords = cursor.fetchall()
    new_json[0] = len(userRecords)
    for i in range(len(userRecords)):
        # print(userRecords[i])
        new_entry = list(userRecords[i])
        temp = {
            "responseID": new_entry[0],
            "userID": new_entry[1],
            "questionID": new_entry[2],
            "response_text": new_entry[3],
            "feedback": new_entry[4],
            "date": new_entry[5],
            "time": new_entry[6],
        }
        new_json[i + 1] = temp

    with open("responses.json", "w") as json_file:
        json_dicts = json.dumps(new_json, default=str)
        json_file.write(json_dicts)

    return userRecords


# create_tables()
# add_questions()
# entries()
# fetch_entries()
# add_questions()
# fetch_responses()
# create_table_responses()
# create_table_outputs()
# fetch_current_user_responses()
