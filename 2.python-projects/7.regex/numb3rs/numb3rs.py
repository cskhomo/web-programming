from re import search


def main():
    
    is_valid = validate(input("IPv4 Address: ")) 
    print(is_valid)


def validate(ip):

    number = "[0-9]{1,3}"
    pattern = fr"^([{number}])\.([{number}])\.([{number}])\.([{number}])$"
    numb3rs = search(pattern, ip)

    if not numb3rs:
        return False

    for numb3r in numb3rs.groups():
         if not 0 <= int(numb3r) <= 255:
             return False
    
    return True


if __name__ == "__main__":
    main()