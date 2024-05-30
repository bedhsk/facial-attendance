import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceattendancerealtime-fd86b-default-rtdb.firebaseio.com/"
})

ref = db.reference("Users")

data = {
    "312654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "212343":
        {
            "name": "Brian Batz",
            "major": "Web",
            "starting_year": 2020,
            "total_attendance": 4,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-04-19 00:54:34"
        },
    "852741":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2018,
            "total_attendance": 5,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-04-19 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 2,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-04-19 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
