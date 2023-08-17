class Config:

    # For openai
    MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 100
    TEMPLATE_PREFIX_TO_OPENAI = "This is the estimate problem - {}," \
                                "ask me questions to make sure that the distinction is indeed correct "

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
