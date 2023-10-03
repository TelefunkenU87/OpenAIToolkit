import argparse
import os

from dotenv import load_dotenv

from models.chat_completion import ChatCompletion


base_dir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(base_dir, 'dev.env')
load_dotenv(dotenv_path=dotenv_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--prompt", help="The prompt to send to the chatbot.")
    parser.add_argument("-m", "--model", help="The model of the chatbot to use.", 
                        choices=['gpt-3.5-turbo', 'gpt-4'], default='gpt-3.5-turbo')
    args = parser.parse_args()

    chat = ChatCompletion(model=args.model)
    user_content = args.prompt

    while True:
        response = chat.post_user_content(user_content)
        print(response)

        user_content = input("Enter additional text (or type 'exit' to end): ")
        
        if user_content.lower() == 'exit':
            break
    
    print("Chat session ended.")


if __name__ == "__main__":
    main()
