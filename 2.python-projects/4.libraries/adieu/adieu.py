import inflect

def main():

    engine = inflect.engine()

    names = list()

    while True:

        try: name = input("Name: ")

        except (EOFError):
            print()
            break

        else:
            names.append(name)
            continue

    print(f"Adieu, adieu, to {engine.join(names)}")

main()
