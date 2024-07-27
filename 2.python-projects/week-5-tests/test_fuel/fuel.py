def main():
    fraction = input("Fraction: ")

    try:
        percentage = convert(fraction)

    except:
        print("Error")

    else:
        print(gauge(percentage))

def convert(fraction):

    x, y = fraction.split("/")

    x = int(x)
    y = int(y)
    
    try:
        quotient = x / y

    except:
        raise ZeroDivisionError

    else:
        if x > y:
            raise ValueError
        else:
            return int(round((quotient*100)))

def gauge(percentage):

    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
