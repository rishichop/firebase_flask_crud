# Testing File

import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate("credentials.json")

def initialize_app():
    firebase_admin.initialize_app(cred, {
        "databaseURL": os.getenv("DATABASE_URI")
    })  

initialize_app()

ref = db.reference("/")
users_ref = ref.child("users")
counter_ref = users_ref.child("counter")


print(counter_ref.get())

print(users_ref.child(f"User{3}"))