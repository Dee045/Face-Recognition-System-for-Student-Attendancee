import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/raute/OneDrive/Desktop/Face-Recognition-System-for-Student-Attendance-main/attendance-cbfc3-firebase-adminsdk-9d2e1-007e89312c.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://attendance-cbfc3-default-rtdb.asia-southeast1.firebasedatabase.app/",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "1": {  # id of student which is a key
        "id": "1",
        "name": "Dharmesh Rautela",
        "password": "1Dharmesh",
        "dob": "2000-10-05",
        "address": "Rto Road, Haldwani",
        "phone": "7648657951",
        "email": "dee@gmail.com",
        "major": "Computer Application",
        "starting_year": 2022,
        "standing": "A",
        "total_attendance": 1,
        "year": 2,
        "last_attendance_time": "2023-11-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
