def main():
    interpreter()

def interpreter():

    expression = input("Provide a Mathematical Expression: ")
    a, operation, b = expression.split(" ")

    match operation:

        case '+':
            print(add(a,b))

        case '-':
            print(subtract(a,b))

        case '*':
            print(multiply(a,b))

        case '/':
            print(round(divide(a,b), 1))

def add(a,b):
    return float(a) + float(b)

def subtract(a,b):
    return float(a) - float(b)

def multiply(a,b):
    return float(a) * float(b)

def divide(a,b):
    return float(a) / float(b)

main()
