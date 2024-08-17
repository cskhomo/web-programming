from re import search


def main():
    hours = parse(input("Hours: "))
    print(hours)


def parse(s):

    pattern = r"([1-9]|1[0-2])(:[0-5][0-9])?( [AP]M)?"
    pattern = f"^{pattern} to {pattern}$"
    
    hours = search(pattern, s)

    try:
        start = list(hours.groups()[:3])
        end = list(hours.groups()[3:])

    except:
        raise ValueError
    
    return f"{convert(start)} to {convert(end)}"


def convert(time):
    
    hours = int(time[0])
    minutes = time[1]

    if " PM" in time:
        if hours != 12:
            hours += 12
    
    elif hours == 12:
        hours = 0

    if not minutes:
        minutes = ":00"

    return f"{hours:02}{minutes}"


if __name__ == "__main__":
    main()