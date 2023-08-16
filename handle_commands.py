from flask import Flask, Response, request
import requests
from main import TOKEN, MESSAGE_URL
#import model.py from NeuralNetwork
from NeuralNetwork.model import predict_image
from firebase.firebase_db import add_user

#import utils.py from NeuralNetwork



def handle_start(user_id, chat_id):
    #TODO: Add code (static or with chatbot) that recieves user name, region, and plant type
    user_name = "David"
    region = "Israel"
    plant_type = "Potato"
    add_user(user_id, user_name, region, plant_type)

def handle_classify(user_id, chat_id, image):
    prediction = predict_image(image)
    print(prediction)





def send_get_request(chat_id, message):
    requests.get(MESSAGE_URL.format(TOKEN, chat_id, message))
