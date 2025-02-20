import openai
import os
from dotenv import load_dotenv

def userInput():
    user_input = input("Enter response (type 'exit' to quit): ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        exit(0)
    if not user_input.strip():
        print("Please enter a valid response.")
        return userInput()
    return {"role": "user", "content": user_input}

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
prime = os.getenv("PROMPT_PRIME")
base_url = os.getenv("BASE_URL")

if not api_key:
    raise ValueError("API key is missing.")
if not prime:
    raise ValueError("Prime is missing.")

client = openai.OpenAI(
    base_url=base_url,
    api_key=api_key
)

messages = [
    {"role": "system", "content": prime}
]

MAX_HISTORY = 10

while True:
    try:
        my_input = userInput()
        messages.append(my_input)
        
        if len(messages) > MAX_HISTORY:
            messages = messages[-MAX_HISTORY:]
        
        completion = client.chat.completions.create(
            model="google/gemini-2.0-flash-thinking-exp:free",
            messages=messages
        )
        print(completion.choices[0].message.content)

        messages.append({"role": "assistant", "content": completion.choices[0].message.content})
        
    except Exception as e:
        print(f"An error occurred: {e}")
        break