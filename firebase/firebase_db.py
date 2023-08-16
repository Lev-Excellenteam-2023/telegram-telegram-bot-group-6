import firebase_admin
from firebase_admin import db
import json


def configure_database():
    cred_obj = firebase_admin.credentials.Certificate('telegrambot-365e7-firebase-adminsdk-fc7ki-3ade0542c6.json')
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': 'https://telegrambot-365e7-default-rtdb.firebaseio.com/'
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
