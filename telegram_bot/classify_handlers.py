from telegram import Update
import requests
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, \
    CallbackContext

from firebase.firebase_db import add_user
from config import Config
from NeuralNetwork.model import predict_image
from telegram_bot import cancel

CLASSIFY = 0
RECEIVE_IMAGE = 1


async def get_image(update: Update, context: CallbackContext):
    # Get the image from the user
    await update.message.reply_text("Please send me a photo of the plant leaf.")
    return CLASSIFY


async def classify_image(update: Update, context: CallbackContext):
    # turn image into byte-like object
    if update.message.photo:
        image = update.message.photo[-1]
        file_id = image.file_id
        file = await context.bot.get_file(file_id)
        file_url = file.file_path
        # download the image
        with open('image.jpg', 'wb') as f:
            f.write(requests.get(file_url).content)
        # classify the image
        # open the image in bytes-like object
        image = open('image.jpg', 'rb').read()
        disease = predict_image(image)

        await update.message.reply_text(f"The disease is {disease}")
        return ConversationHandler.END

classify_conv = ConversationHandler(
    entry_points=[CommandHandler('classify', get_image)],
    states={
        CLASSIFY: [
            MessageHandler(None, callback=classify_image)],
        RECEIVE_IMAGE: [MessageHandler(None, callback=get_image)]
    },
    fallbacks=[CommandHandler('cancel', cancel)])
