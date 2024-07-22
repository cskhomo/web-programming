def main():
    statement = input("Make a statement: ")
    print(convert(statement))

def convert(statement):
    emoji_statement = statement.replace(":)","🙂").replace(":(","🙁")
    return emoji_statement

main()
