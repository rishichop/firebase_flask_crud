import firebase_admin
from firebase_admin import credentials
import os
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate("credentials.json")

def initialize_app():
    firebase_admin.initialize_app(cred, {
        "databaseURL": os.getenv("DATABASE_URI")
    })  

# ref = db.reference("/")
# users_ref = ref.child("users")
# users_ref.set({
#     "rishikesh": {
#         "date_of_birth": "September 1, 2003",
#         "Full_name": "Rishikesh Chopade"
#     }
# })


