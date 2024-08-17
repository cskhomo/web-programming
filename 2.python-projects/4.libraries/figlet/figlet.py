from pyfiglet import Figlet
from random import choice
from sys import argv
from sys import exit


def main():

    figlet = Figlet()
    figFonts = figlet.getFonts()

    if len(argv) == 1:

        figlet.setFont(font=choice(figFonts))
        print(f"Output: \n{figlet.renderText(input('Input: '))}")
        exit()

    if len(argv) == 3:
        if argv[1] == '-f' or argv[1] == '--font':
            if argv[2] in figFonts:

                figlet.setFont(font=argv[2])
                print(f"Output: \n{figlet.renderText(input('Input: '))}")
                exit()

    exit("Invalid Argument(s)!!")

main()
