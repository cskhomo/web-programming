from emoji import emojize

def main():

    message = input('Input: ')
    print(f"Output: {text_to_emoji(message)}")

def text_to_emoji(text):
    return  emojize(text, language='alias')

main()
