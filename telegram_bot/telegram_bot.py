from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

from firebase.firebase_db import add_user
from config import Config
import classify_handlers
from gpt_handlers import gpt_conv

PHONE = 0
COUNTRY = 1
CITY = 2

COMMAND_DESCRIPTION = {
    '/start': 'Start the conversation with the bot',
    '/openchat': 'Open a new chat and provide your phone number, country, and city',
    '/cancel': 'Cancel the current conversation',
    '/classify': 'Classify an image of a plant leaf',
    '/help': 'Display this help message'
}


# Command handler for the /start command
async def start_command(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Hi! Thanks for chatting with me!\nI am the Plant diseases detector"
        " Bot. Please type /help to see the available commands.")


# Command handler for the /help command
async def help_command(update: Update, context: CallbackContext) -> int:
    help_text = "Here are the available commands:\n\n"
    for command, description in COMMAND_DESCRIPTION.items():
        help_text += f"{command}: {description}\n"

    await update.message.reply_text(help_text)


# Command handler for the /cancel command
async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END


# Command handler for the /openchat command
async def open_new_chat_command(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Okay, before we continue, let's start with your phone number please.")
    return PHONE


# Function gets phone number from user and saves it to user_data
async def get_phone(update: Update, context: CallbackContext) -> int:
    phone = update.message.text
    chat_id = update.message.chat_id  # Get the chat ID of the user
    context.user_data['phone'] = phone
    await context.bot.send_message(chat_id, "Please send your country")
    return COUNTRY


# Function gets country from user and saves it to user_data
async def get_country(update: Update, context: CallbackContext) -> int:
    country = update.message.text
    context.user_data['country'] = country
    await context.bot.send_message(update.message.chat_id, "Please send your city")
    return CITY


# Function gets city from user and saves it to user_data
async def get_city(update: Update, context: CallbackContext) -> int:
    city = update.message.text
    context.user_data['city'] = city

    # Get user information from user_data
    phone = context.user_data['phone']
    country = context.user_data['country']

    # Call your add_user function to save data to your database
    add_user(phone, update.effective_user.full_name, country, city)  # Modify this line according to your function

    await context.bot.send_message(update.message.chat_id, "Thank you! Your information has been saved.")
    return ConversationHandler.END


def main():
    app = ApplicationBuilder().token(Config.TELEGRAM_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('openchat', open_new_chat_command)],
        states={
            PHONE: [MessageHandler(filters.Text and filters.Regex(r'^(?!/)') and filters.Regex(r'^\d+$'), get_phone)],
            COUNTRY: [MessageHandler(filters.Text and filters.Regex(r'^(?!/)'), get_country)],
            CITY: [MessageHandler(filters.Text and filters.Regex(r'^(?!/)'), get_city)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]

    )
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(gpt_conv)
    app.add_handler(classify_handlers.classify_conv)
    app.add_handler(conv_handler)
    app.run_polling()


if __name__ == '__main__':
    main()