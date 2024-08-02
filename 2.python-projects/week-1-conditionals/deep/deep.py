def main():
    deep()

def deep():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    formatted_answer = answer.strip().lower()

    match formatted_answer:

        case "42" | "forty two" | "forty-two":
            print("Yes")

        case _ :
            print("No")

main()
