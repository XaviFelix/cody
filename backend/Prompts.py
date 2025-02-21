# This needs to append the list to the main prompt
# TODO: Create a main prompt
# get main propmt using env var and store into a string
# then append from there

def promptLLM(selected_options):
    appnedToMainPrompt = " ".join(selected_options)

    print("These are the words coming from promptLLM():")
    print(appnedToMainPrompt)
    # updatePrompt(appnedToMainPrompt)