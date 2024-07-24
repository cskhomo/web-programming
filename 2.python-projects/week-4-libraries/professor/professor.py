import random

def main():

    level = get_level()
    score = generate_integer(level)

    print(f"Score: {score}")

def get_level():

    while True:

        try: level = int(input("Level: "))

        except: continue

        else:
            if 1 <= level <= 3:
                return level

def generate_integer(level):

    start = [0, 10, 100][level-1]
    stop = 10**level - 1
    score = 10

    for i in range(10):

        x = random.randint(start,stop)
        y = random.randint(start,stop)
        trials = 3
        z = x + y

        while trials != 0:

            if str(z) == input(f"{x} + {y} = "): break

            else: print("EEE")

            trials -= 1

            if trials == 0:
                print(f"{x} + {y} = {z}")
                score -= 1

    return score

if __name__ == "__main__":
    main()