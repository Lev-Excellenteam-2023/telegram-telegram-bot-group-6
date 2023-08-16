import firebase_admin
from firebase_admin import db
from config import Config
import json

with open(r'C:\Users\User\Desktop\exellenteam\bot\telegram-telegram-bot-group-6\firebase\.env', "r") as file:
    SERVICE_ACCOUNT_KEY = file.read().strip()


def configure_database():
    cred_obj = firebase_admin.credentials.Certificate(SERVICE_ACCOUNT_KEY)
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': Config.FIREBASE_URL
    })


def add_user(phone: str, full_name: str, location_country: str, location_city: str):
    users_ref.child(phone).set({
        'full_name': full_name,
        'location_country': location_country,
        'location_city': location_city
    })


if __name__ == "__main__":
    configure_database()
    ref = db.reference("/")
    users_ref = db.reference("/Users")
    add_user('0521234567', 'Yheuda', 'Israel', 'harish')
