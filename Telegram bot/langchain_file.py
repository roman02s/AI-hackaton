import os
import openai
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


def get_completion(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": combined_prompt},
    ],
        temperature=0,
    )
    return response.choices[0].message["content"]
