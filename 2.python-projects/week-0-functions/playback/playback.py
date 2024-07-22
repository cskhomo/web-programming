def main():
    playback()

def playback():
    statement = input("Make a statement: ")
    slow_statement = statement.replace(" ", "...")
    print(slow_statement)

main()
