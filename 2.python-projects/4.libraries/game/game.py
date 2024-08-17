from random import randint

def main():

    while True:

        try: target = randint(1, int(input("Level: ")))

        except (ValueError): continue

        else: break

    while True:

        try: guess = int(input("Guess: "))

        except (ValueError): continue

        else:

            if guess > target:
                print("Too large!")

            elif guess < target:
                print("Too small!")

            else: break

            continue

    print("Just right!")

    exit()

main()
