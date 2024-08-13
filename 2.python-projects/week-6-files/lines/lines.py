from sys import argv, exit
from check_args import *


def main():
    
    file_status = check_args(argv, 2, ".py")

    if file_status.startswith("!"):
        exit(file_status[1::])
    
    lines = count_lines(file_status)
    
    if lines == -1:
        exit("File does not exist")
    
    print(lines)


def count_lines(file):
    
    count = 0

    try:
        with open(file) as script:
            for line in script:
                if line.lstrip().startswith("#"):
                    continue
                if len(line.rsplit()) > 0:
                    count += 1

    except FileNotFoundError:
        count = -1
    
    return count


if __name__ == "__main__":
    main()