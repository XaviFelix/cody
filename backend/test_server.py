from dotenv import load_dotenv
import os, openai, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from FileLogger import FileLogger


def callLLM(userInput, messages, api_key, base_url, displayBox):
    MAX_HISTORY = 10
    if len(messages) > MAX_HISTORY:
        messages = messages[-MAX_HISTORY:]

    element = {"role": "user", "content": userInput}

    # I feel like this needs to be loaded once
    # load_dotenv()
    # api_key = os.getenv("OPENAI_API_KEY")
    # base_url = os.getenv("BASE_URL")

    if not api_key:
        raise ValueError("API key is missing.")

    client = openai.OpenAI(
        base_url=base_url,
        api_key=api_key
    )
    messages.append(element)

    completion = client.chat.completions.create(
        model="google/gemini-2.0-flash-thinking-exp:free",
        messages=messages
    )
    print(completion.choices[0].message.content) #Shows up on console
    # Make it show up on display now
    displayBox.updateDisplay(completion.choices[0].message.content)

    # Append to message history
    # also have a section in the message list where it keeps track of the current
    # topics to ask about
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})


def userInput():
    user_input = input("Enter response (type 'exit' to quit): ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        exit(0)
    if not user_input.strip():
        print("Please enter a valid response.")
        return userInput()
    return {"role": "user", "content": user_input}


def callLLM_test(messages, llmTester):
    llmTester.debug("callLLM_test() is being called")
    user_input = userInput()
    MAX_HISTORY = 10
    if len(messages) > MAX_HISTORY:
        messages = messages[0:1]

    # I feel like this needs to be loaded once
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("BASE_URL")

    if not api_key:
        raise ValueError("API key is missing.")

    client = openai.OpenAI(
        base_url=base_url,
        api_key=api_key
    )
    llmTester.debug("Messages before adding user input:")
    llmTester.debug(messages)
    messages.append(user_input)
    llmTester.debug("Messagse after adding user input:")
    llmTester.debug(messages)

    completion = client.chat.completions.create(
        model="google/gemini-2.0-flash-thinking-exp:free",
        messages=messages
    )
    print(completion.choices[0].message.content) #Shows up on console
    # Make it show up on display now

    # Append to message history
    # also have a section in the message list where it keeps track of the current
    # topics to ask about
    messages.append({"role": "assistant", "content": completion.choices[0].message.content.strip()})
    llmTester.debug("Messages after adding AI's response: ")
    llmTester.debug(messages)




if __name__ == '__main__': 
    load_dotenv()
    prime = os.getenv("PROMPT_PRIME")
    messages = [
        {"role": "system", "content": prime}
    ]

    llmTester = FileLogger("llmTester.log")
    # callLLM_test(messages, llmTester)
    while True:
        callLLM_test(messages, llmTester)





