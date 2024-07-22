SPEED_OF_LIGHT = 300000000 #meters per second

def main():
    einstein()

def einstein():
    mass = int(input("Provide a mass in Kg: "))
    energy = mass * pow(SPEED_OF_LIGHT, 2)
    print(f"E: {energy}")

main()
