from telegram import Update
import requests
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, CallbackContext

from NeuralNetwork.model import predict_image
from gpt.openai_request import async_ask_openai




# Function prompts user to send an image
async def haveConversation(update: Update, context: CallbackContext) -> int:
    # Get the image from the user
    await update.message.reply_text("What is your problem?")
    
