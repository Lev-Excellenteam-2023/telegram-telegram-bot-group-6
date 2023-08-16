import openai
from config import Config
import asyncio


with open(r'C:\Users\User\Desktop\exellenteam\bot\telegram-telegram-bot-group-6\openai\.env', "r") as file:
    OPENAI_KEY = file.read().strip()
openai.api_key = OPENAI_KEY


def generate_prompt(estimate_problem):
    return Config.TEMPLATE_PREFIX_TO_OPENAI.format(estimate_problem)


async def async_ask_openai(messages):

    try:
        response = await openai.ChatCompletion.acreate(
            model=Config.MODEL,
            max_tokens=Config.MAX_TOKENS,
            messages=messages,
            timeout=Config.TIMEOUT
        )
        content = response.choices[0].message.content
        print(content)
        messages.append({"role": "assistant", "content": content})
        return content

    except openai.error.RateLimitError as e:
        print(f'api key get to the limit msg:{e}')

    except openai.error.Timeout as e:
        print(f'openai time out :{e}')

    except openai.error.AuthenticationError as e:
        print(f'invalid openAI token: {e}')


async def main():

    messages = [{"role": "system", "content": "You need to verify the correctness of the disease"}]
    prompt = generate_prompt('Apple Rusk')
    messages.append({"role": "user", "content": prompt})
    await async_ask_openai(messages)

    while True:
        user_input = input(" ")
        messages.append({"role": "user", "content": user_input})
        await async_ask_openai(messages)
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())