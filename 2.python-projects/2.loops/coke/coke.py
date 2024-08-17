def main():

    coke()

def coke():

    due = 50

    while (due > 0):

        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))

        match coin:

            case 5 | 10 | 25:
                due -= coin

    print(f"Change Owed: {-due}")

main()
