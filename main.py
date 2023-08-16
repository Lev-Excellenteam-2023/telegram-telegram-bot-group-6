from flask import Flask, Response, request
import requests

import handle_commands

TOKEN = "6313275275:AAGfL-IMwcOnk7HllN9pFW7XtV8LJYNnCqU"

NGROK_URL = "https://8ff5-2a01-6500-a046-f352-a0ff-cd65-3597-6b28.ngrok-free.app"
TELEGRAM_INIT_WEBHOOK_URL = "https://api.telegram.org/bot{}/setWebhook?url={}/message".format(TOKEN, NGROK_URL)
MESSAGE_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"


requests.get(TELEGRAM_INIT_WEBHOOK_URL)

app = Flask(__name__)


@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    json = request.get_json()
    user_id = request.get_json()['message']['from']['id']
    chat_id = request.get_json()['message']['chat']['id']
    # #check if there is an image
    # if json['message'].get('photo'):
    #     image = request.get_json()['message']['photo'][0]['file_id']
    #     #Open image in byte-like object
    #     image = requests.get("https://api.telegram.org/bot{}/getFile?file_id={}".format(TOKEN, image)).json()['result']['file_path']
    #     handle_commands.handle_classify(user_id, chat_id, image)
    #     return
    message = request.get_json()['message']['text']
    if message == "/start":
        handle_commands.handle_start(user_id, chat_id)



    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
