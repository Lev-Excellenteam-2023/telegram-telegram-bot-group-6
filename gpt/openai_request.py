import openai
from NeuralNetwork.utils import disease_dic
from firebase.firebase_db import get_user, root_ref
from config import Config
import asyncio


with open(r'./env', "r") as file:
    OPENAI_KEY = file.read().strip()
openai.api_key = OPENAI_KEY


def generate_prompt(estimate_problem):
    estimate_problem_info = generate_condition_info()
    return Config.TEMPLATE_PREFIX_TO_OPENAI.format(estimate_problem)


def generate_condition_info(condition):
    condition_info = disease_dic[condition]
    print(condition_info)
    return condition_info


async def async_ask_openai(messages):
    try:
        response = await openai.ChatCompletion.acreate(
            model=Config.MODEL,
            max_tokens=Config.MAX_TOKENS,
            messages=messages,
            timeout=Config.TIMEOUT
        )
        return response.choices[0].message.content

    except openai.error.RateLimitError as e:
        print(f'api key get to the limit msg:{e}')

    except openai.error.Timeout as e:
        print(f'openai time out :{e}')

    except openai.error.AuthenticationError as e:
        print(f'invalid openAI token: {e}')

async def main():
    conversation_history = []
    while True:
        user_message = input("You: ")  # Get user input
        conversation_history += f"User: {user_message}"
        response = await async_ask_openai(conversation_history)  # Generate bot's response

        bot_message = response.choices[0].text.strip()  # Get bot's response
        conversation_history += f"\nBot: {bot_message}"  # Append bot's response to history
        print("Bot:", bot_message)  # Print bot's response


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
