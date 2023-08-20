from flask import Flask, Response, request
import requests
from config import Config
import handle_commands


requests.get(Config.TELEGRAM_INIT_WEBHOOK_URL)
app = Flask(__name__)


@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    json = request.get_json()
    user_id = request.get_json()['message']['from']['id']
    chat_id = request.get_json()['message']['chat']['id']
    message = request.get_json()['message']['text']
    if message == "/start":
        handle_commands.handle_start(user_id, chat_id)



    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
