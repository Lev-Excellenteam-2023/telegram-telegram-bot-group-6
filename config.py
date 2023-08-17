class Config:

    # For openai
    MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 500
    TIMEOUT = 2
    TEMPLATE_PREFIX_TO_OPENAI = "Hi openai, the user grows plants, but there is a disease there." \
                                "The estimate disease is {}." \
                                "I want you to make sure that the distinction is indeed correct." \
                                "You will ask the user questions, only one question at a time," \
                                "and based on his answer you will understand whether and what more needs" \
                                "to be asked of him," \
                                "until you come to the conclusion that the distinction is correct," \
                                "or you say that according to the data you do not know what the correct distinction" \
                                "is in his case. Don't write thank tou, sure, or something else," \
                                "ask only focused and short questions, and just after you think that this is the" \
                                "correct distinction, write it." \
                                "This is the information about this disease: {}." \

    # For Telegram bot
    with open(r'C:\Users\yehuda\Documents\ExcelenTeam\Plant-Telegram-Bot\env', "r") as file:
        TELEGRAM_TOKEN = file.read().strip()
    NGROK_URL = "https://8ff5-2a01-6500-a046-f352-a0ff-cd65-3597-6b28.ngrok-free.app"
    TELEGRAM_INIT_WEBHOOK_URL = "https://api.telegram.org/bot{}/setWebhook?url={}/message".format(TELEGRAM_TOKEN, NGROK_URL)
    MESSAGE_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"

    # For firebase
    FIREBASE_URL = 'https://telegrambot-365e7-default-rtdb.firebaseio.com/'

    SERVICE_ACCOUNT_KEY = r'C:\Users\yehuda\Documents\ExcelenTeam\Plant-Telegram-Bot\firebase\telegrambot-365e7-firebase-adminsdk-fc7ki-3ade0542c6.json'
    DATABASE_URL = 'https://telegrambot-365e7-default-rtdb.firebaseio.com/'

    # For NeuralNetwork
    IMAGE_PATH = r'./user_images/'
