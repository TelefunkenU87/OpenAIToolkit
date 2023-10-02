import json
import os
import requests

import openai

_api_key_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DO-NOT-COMMIT.txt'))

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def post_chat_completion(prompt:str, model:str='gpt-3.5-turbo', agent_promt:str='You are a helpful assistant.'):
    openai.api_key = read_file(_api_key_file)

    chat_completion_response = openai.ChatCompletion.create(
        model=model, 
        messages=[
            {"role": "system", "content": f"{agent_promt}"},
            {"role": "user", "content": f"{prompt}"}
            ])
    
    response = chat_completion_response['choices'][0]['message']['content'] # type: ignore

    return response


test_message = "Hello, I'm testing this out. Please let me know if you can see this message."

response = post_chat_completion(test_message)

print(response)