def main():

    Total = 0

    menu = {
              "Baja Taco": 4.25,
              "Burrito": 7.50,
              "Bowl": 8.50,
              "Nachos": 11.00,
              "Quesadilla": 8.50,
              "Super Burrito": 8.50,
              "Super Quesadilla": 9.50,
              "Taco": 3.00,
              "Tortilla Salad": 8.00,
            }

    while True:

        try:
            food = input("Item: ").title()

        except EOFError:
            print()
            break

        else:
            try: price = menu[food]

            except KeyError: continue

            else:
                Total += price
                print(f"Total: ${Total:.2f}")
main()
