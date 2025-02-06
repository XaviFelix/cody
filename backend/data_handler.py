# backend/data_handler.py

def process_input(user_input):
    """
    Process the user input. 
    For now, we simply return the input in uppercase.
    Later, this function could be extended to call an API.
    """
    # For fun, let's reverse the string too!
    return f"{user_input.upper()} | {user_input[::-1]}"
