from re import findall


def main():
    um = count(input("Text: "))
    print(um)


def count(s):

    pattern = r"\bum\b"
    um = findall(pattern, s)
  
    return len(um)


if __name__ == "__main__":
    main()