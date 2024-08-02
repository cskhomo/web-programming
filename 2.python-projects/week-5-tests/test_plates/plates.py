def main():

    plate = getPlate("Plate: ")

    if is_valid(plate):
        print("Valid")

    else: print("Invalid")

def getPlate(prompt):
    return input(prompt)

def is_valid(s):

    Bool = False

    if 2 <= len(s) <= 6: # Between 2 and 6 characters

        if s[:2].isalpha(): # Start with 2 letters

            if s.isalnum(): # Has no symbols

                Bool = True

                for c in s:

                    try: i = int(c)

                    except: pass

                    else:

                        if c.isnumeric():
                            if s[s.find(c):].isnumeric(): # Numbers at the end
                                Bool = True
                            else:
                                Bool = False
                                break

                            if i == 0:  # No zero start
                                if s[s.find(c)-1].isnumeric():
                                    Bool = True

                                else:
                                    Bool = False
                                    break
    return Bool

if __name__ == "__main__":
    main()