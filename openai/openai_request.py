import openai
from config import Config


with open(r'C:\Users\User\Desktop\exellenteam\bot\telegram-telegram-bot-group-6\openai\.env', "r") as file:
    OPENAI_KEY = file.read().strip()
openai.api_key = OPENAI_KEY


def generate_prompt(estimate_problem):
    return Config.TEMPLATE_PREFIX_TO_OPENAI.format(estimate_problem)


def ask_openai(prompt):
    response = openai.ChatCompletion.create(
        model=Config.MODEL,
        max_tokens=Config.MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)


def main():
    prompt = generate_prompt('Apple Rusk')
    ask_openai(prompt)


if __name__ == "__main__":
    main()