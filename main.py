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
    user_id = request.get_json()['message']['from']['id']
    chat_id = request.get_json()['message']['chat']['id']
    message = request.get_json()['message']['text']
    print(message)
    if message == "/start":
        handle_commands.handle_start(user_id, chat_id)
    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
