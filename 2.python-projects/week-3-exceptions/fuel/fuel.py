def main():
    percentage = getPercentage()
    getFuel(percentage)

def getPercentage():

    while True:
        fraction = input("Fraction: ")

        if '/' in fraction:
            x, y = fraction.split('/')

        else: continue

        try:
           quotient = int(x) / int(y)

        except (ValueError, ZeroDivisionError):
            continue

        else:
            if quotient > 1: continue

            else : return int(round((quotient*100)))

def getFuel(percentage):

    if percentage <= 1:
        print("E")

    elif percentage >= 99:
        print("F")

    else:
        print(f"{percentage}%")

main()
