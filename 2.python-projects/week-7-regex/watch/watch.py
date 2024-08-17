from re import search


def main():
    url = parse(input("HTML: "))
    print(url)


def parse(s):

    pattern = r'http(?:s)?://(?:www\.)?youtube\.com/embed/(.+)"'
    url = search(pattern, s)

    if not url:
        return None
    
    return f"https://youtu.be/{url.group(1)}"


if __name__ == "__main__":
    main()