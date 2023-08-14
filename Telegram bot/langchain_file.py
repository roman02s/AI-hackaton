import os
import openai
from dotenv import load_dotenv, find_dotenv

os.environ['OPENAI_API_KEY'] = "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"

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
