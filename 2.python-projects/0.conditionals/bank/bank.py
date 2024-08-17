def main():
    bank()

def bank():

    greeting = input("Provide a greeting: ")

    formatted_greeting = greeting.strip().lower()

    if formatted_greeting.startswith("hello"):
        print("$0")

    elif formatted_greeting.startswith('h'):
        print("$20")

    else : print("$100")

main()
