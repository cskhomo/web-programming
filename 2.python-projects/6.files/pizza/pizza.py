from sys import argv, exit
from csv import reader
from check_args import *
from tabulate import *


def main():
    
    file_status = check_args(argv, 2, ".csv")

    if file_status.startswith("!"):
        exit(file_status.strip("!"))
    
    table = make_table(file_status)

    if table == -1:
        exit("File does not exist")
    
    print(table)

    
def make_table(file):

    table = []

    try:
        with open(file) as menu:
            for row in reader(menu):
                table.append(row)

    except FileNotFoundError:
        return -1
    
    return tabulate(table[1:], table[0], tablefmt="grid")


if __name__ == "__main__":
    main()