def main():
    camel()

def camel():

    camel_case = input("camelCase: ")
    snake_case = str()

    for char in camel_case:

        if char.islower():
            snake_case += char

        else:
            snake_case += "_" + char.lower()

    print(f"snake_case: {snake_case}")

main()
