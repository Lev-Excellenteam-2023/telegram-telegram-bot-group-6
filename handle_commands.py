from flask import Flask, Response, request
import requests
from config import Config


def handle_start(user_id, chat_id):
    #TODO: Add code (static or with chatbot) that recieves user name, region, and plant type
    user_name = "David"
    region = "Israel"
    plant_type = "Potato"
    save_user(user_id, user_name, region, plant_type)


def send_get_request(chat_id, message):
    requests.get(Config.MESSAGE_URL.format(Config.TELEGRAM_TOKEN, chat_id, message))
