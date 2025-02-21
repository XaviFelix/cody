import openai
import os
from dotenv import load_dotenv
import logging

# Refactor this into its own file or class so that i can use it around the project
current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, 'envVarLog.log')

# Setting up logger for testing
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(log_file_path, mode='w')
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
# End of logger set-up

# Used to ensure the variables are valid
def validateVariables(api_key, prime, base_url):
    if not api_key:
        raise ValueError("API key is missing.")
    if not prime:
        raise ValueError("Prime is missing.")
    if not base_url:
     raise ValueError("Base URL is missing")

    # Logging the tests onto a log file
    logger.info("Calling from validateVariables()")
    logger.info("Variables validated")
    logger.info(f"This is the api Key: {api_key}")
    logger.info(f"This is the base URL: {base_url}")
    logger.info(f"This is the prime: {prime}")

    # print("Variables validated")
    # print(f"This is the api key: {api_key}")
    # print(f"This is the prime: {prime}")
    # print(f"This is the base URL: {base_url}")

    
# used when the env vars are needed by a function
def loadVariables():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    prime = os.getenv("PROMPT_PRIME")
    base_url = os.getenv("BASE_URL")

    validateVariables(api_key, prime, base_url)

    return api_key, prime, base_url

#TODO: Needs testing
def updatePrompt(updated_string):
    print("Updating prompt")

def userInput():
    user_input = input("Enter response (type 'exit' to quit): ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        exit(0)
    if not user_input.strip():
        print("Please enter a valid response.")
        return userInput()
    return {"role": "user", "content": user_input}

# It seems like i might need to use Qthreads as well as signals
def startCody(displayBox=None, enterButton=None):
    api_key, prime, base_url = loadVariables()
    logger.info("Calling from callLLM()")
    logger.info(f"This is the thread: {displayBox}")
    logger.info(f"This is the api Key: {api_key}")
    logger.info(f"This is the base URL: {base_url}")
    logger.info(f"This is the prime: {prime}")

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
            if enterButton:
                print("enter button was pressed here")
            else:
                my_input = userInput()
                messages.append(my_input)
            
            # This clears the history
            if len(messages) > MAX_HISTORY:
                messages = messages[-MAX_HISTORY:]
            
            # Builds the completion 
            completion = client.chat.completions.create(
                model="google/gemini-2.0-flash-thinking-exp:free",
                messages=messages
            )
            # Prints to display box if reference to it is passed, printed to console too
            if displayBox:
                # Change instead call the handler form the display box
                displayBox.setText(completion.choices[0].message.content)
            print(completion.choices[0].message.content)

            # append to message history
            messages.append({"role": "assistant", "content": completion.choices[0].message.content})
            
        except Exception as e:
            logger.info(f"Exception, this is what my input has: {my_input}")
            print(f"An error occurred: {e}")
            break