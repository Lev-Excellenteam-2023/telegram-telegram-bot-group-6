from telegram import Update
import requests
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, CallbackContext

from NeuralNetwork.model import predict_image
from gpt.openai_request import async_ask_openai, generate_prompt
import asyncio

START = 0
CONTINUE = 1


messages = [{"role": "system", "content": "You need to verify the correctness of the disease"}]

# Function prompts user to send an image
async def haveConversation(update: Update, context: CallbackContext) -> int:
    # Get the image from the user
    prompt = generate_prompt(context.user_data['disease'])
    messages.append({"role": "user", "content": prompt})
    answer = await async_ask_openai(messages)
    messages.append({"role": "system", "content": answer})
    await update.message.reply_text(answer)
    return CONTINUE

async def continueConversation(update: Update, context: CallbackContext) -> int:
    # Get the image from the user
    user_response = update.message.text
    if user_response == "/stop":
        await update.message.reply_text("Conversation canceled.")

        return ConversationHandler.END
    messages.append({"role": "user", "content": user_response})
    answer = await async_ask_openai(messages)
    messages.append({"role": "system", "content": answer})
    await update.message.reply_text(answer)
    return CONTINUE

async def stopConversation(update: Update, context: CallbackContext):
    await update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END

gpt_conv = ConversationHandler(
    entry_points=[CommandHandler('talk', haveConversation)],
    states={
        CONTINUE: [
            MessageHandler(None, callback=continueConversation)],
    },
    fallbacks=[CommandHandler('stop', stopConversation)])

