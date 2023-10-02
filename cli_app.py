import argparse
from chat_completions import core

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--prompt", help="The prompt to send to the chatbot.")
    parser.add_argument("-m", "--model", help="The model of the chatbot to use.", 
                        choices=['gpt-3.5-turbo', 'gpt-4'], default='gpt-3.5-turbo')
    args = parser.parse_args()

    response = core.post_chat_completion(args.prompt)

    print(response)