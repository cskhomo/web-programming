def main():

    greeting = input("Provide a greeting: ")
    print(f"${value(greeting)}")

def value(greeting):

    formatted_greeting = greeting.strip().lower()
    payout = int()

    if formatted_greeting.startswith("hello"):
        payout = 0

    elif formatted_greeting.startswith('h'):
        payout =  20

    else : payout = 100

    return payout

if __name__ == "__main__":
    main()