import openai
import os

# Set your OpenAI API key here or use an environment variable
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

openai.api_key = api_key

def hello_openai():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, world!"}
        ]
    )
    print("OpenAI response:", response['choices'][0]['message']['content'].strip())

if __name__ == "__main__":
    hello_openai()
