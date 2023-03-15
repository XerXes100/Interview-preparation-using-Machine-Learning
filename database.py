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
    
def create_tables():
    
    
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
        "CREATE TABLE IF NOT EXISTS users ( \
            userID INT PRIMARY KEY, \
            username VARCHAR (255), \
            email VARCHAR(255), \
            password VARCHAR(255), \
            isLoggedIn BOOL \
        );"
    )
    
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS questions ( \
            questionID INT PRIMARY KEY, \
            question VARCHAR(1000), \
            ideal_answer VARCHAR(3000) \
        );"
    )

    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS responses ( \
    #         responseID INT PRIMARY KEY, \
    #         userID INT, \
    #         questionID INT, \
    #         response_text VARCHAR(1000), \
    #         response_audio BLOB, \
    #         feedback VARCHAR(1000), \
    #         date DATE, \
    #         time TIME, \
    #         CONSTRAINT fk1 FOREIGN KEY (userID) REFERENCES users(userID) ON UPDATE CASCADE ON DELETE CASCADE, \
    #         CONSTRAINT fk2 FOREIGN KEY (questionID) REFERENCES questions(questionID) ON UPDATE CASCADE ON DELETE CASCADE \
    #     );"
    # )
    
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
    sql_insert_user = "INSERT INTO users(userID, username, email, password, isLoggedIn) VALUES(%s,%s,%s,%s,%s)"

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
    
def add_questions():
    sql_insert_questions = "INSERT INTO questions(questionID, question, ideal_answer) VALUES(%s,%s,%s)"
    qvalues = [
        (
            1,
            "Tell me about yourself",
            "My name is Jane Smith, and I am a final year engineering student at Duke University, majoring in Electrical Engineering. I have a strong passion for developing innovative solutions to real-world problems through my studies in engineering. I have completed various projects and internships in the field of power systems, renewable energy, and control systems. I have a strong interest in the field of machine learning and have taken relevant courses to further my knowledge in this area. I am a highly motivated individual who is always eager to take on new challenges and expand my skill set. I aim to work in a research and development role where I can continue to learn and innovate in the field of engineering. Outside of my studies, I am an active member of the robotics club, where I have been a team lead for the past two years."
        ),
        (
            2,
            "What are your strengths?",
            "xxx"
        ),
        (
            3,
            "Where do you see yourself in the future?",
            "I am passionate about using my skills in technology to make a positive impact on society, and I see myself continuing to work in this field in the future. As the industry evolves, I plan to keep up with the latest developments and continue learning new technologies. Ultimately, I hope to become a respected leader in the field, mentoring and guiding others to develop innovative solutions to important problems"
        )
    ]
    cursor.executemany(sql_insert_questions, qvalues)
    mydb.commit()

def fetch_entries():
    cursor.execute("select * from users")
    userRecords = cursor.fetchall()
    for i in range(len(userRecords)):
        print(userRecords[i])
    

def user_entry(username, email, password):
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
        

def fetch_entry(email, password):
    
    fetch_user = f"SELECT * FROM users WHERE email = %s and password = %s;"
    fetch_values = [email, password]
    cursor.execute(fetch_user, fetch_values)
    userRecords = cursor.fetchall()
    
    print(userRecords)

    if (len(userRecords) == 1):
        (userID_fetched, username_fetched, email_fetched, password_fetched, isLoggedIn) = userRecords[0]
        return {"userID" : userID_fetched,
                "username": username_fetched,
                "email": email_fetched,
                "password" : password_fetched,
                "isLoggedIn": isLoggedIn
                }
    else:
        return {"userID" : "",
                "username": "",
                "email": "",
                "password" : "",
                "isLoggedIn": ""
                }

def add_response(response, current_date, current_time):
    f = open('user.json')

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
    
    sql_insert_response = f"INSERT INTO responses(\
        responseID, \
        userID, \
        questionID, \
        response_text, \
        feedback, \
        date, \
        time) VALUES \
        (%s, %s, %s, %s, %s, %s, %s);"
    
    response_values = [
        response_id,
        data["userID"],
        1,
        response,
        feedback_text,
        current_date,
        current_time
    ]
    
    cursor.execute(sql_insert_response, response_values)

    mydb.commit()
    print("Response added successfully")

def check_responses():
    cursor.execute("select * from responses")
    userRecords = cursor.fetchall()
    for i in range(len(userRecords)):
        print(userRecords[i])
    

# create_tables()
# add_questions()
# entries()
# fetch_entries()
# add_questions()
# check_responses()
