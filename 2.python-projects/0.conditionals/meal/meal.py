def main():

    time = input("What time is it? - ")

    hours_passed = convert(time)

    if 7.0 <= hours_passed <= 8.0:
        print("breakfast time")

    elif 12.0 <= hours_passed <= 13.0:
        print("lunch time")

    elif 18.0 <= hours_passed <= 19.0:
        print("dinner time")

def convert(time):

    hours, minutes = time.split(":")
    hours_passed = float(hours) + float(minutes)/60
    return hours_passed

if __name__ == "__main__":
    main()
