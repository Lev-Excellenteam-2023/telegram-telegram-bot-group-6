import openai

from NeuralNetwork.utils import disease_dic
from firebase.firebase_db import get_user, root_ref
from config import Config


with open(r'C:\Users\yehuda\Documents\ExcelenTeam\Plant-Telegram-Bot\openai\env', "r") as file:
    OPENAI_KEY = file.read().strip()
openai.api_key = OPENAI_KEY


def generate_prompt(estimate_problem):
    return Config.TEMPLATE_PREFIX_TO_OPENAI.format(estimate_problem)

def generate_condition_info(condition):
    condition_info = disease_dic[condition]
    print(condition_info)
    return condition_info


def ask_openai(prompt):
    response = openai.ChatCompletion.create(
        model=Config.MODEL,
        max_tokens=Config.MAX_TOKENS,
        messages=[{"role": "assistant", "content": "These are the conditions of the problem: " + prompt}, {"role": "user", "content": "What should i do?"}]
    )
    print(response.choices[0].message.content)


def main():
    prompt = generate_prompt('Apple Rusk')
    user_info = get_user('123456')
    print(root_ref.get())
    location = user_info['location_country']
    print(location)
    condition = 'Apple___Cedar_apple_rust'
    condition_info = generate_condition_info(condition)
    ask_openai(condition_info)


if __name__ == "__main__":
    main()