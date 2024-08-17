from sys import argv, exit
from csv import DictReader, DictWriter
from check_args import *


def main():

    file_status = check_args(argv, 3, ".csv")

    if file_status.startswith("!"):
        exit(file_status.strip("!"))

    try:
        clean_data(file_status, argv[2])

    except FileNotFoundError:
        exit(f"Could not read {file_status}")


def clean_data(in_file, out_file):

    with open(in_file, "r") as in_data, open(out_file, "w") as out_data:
        writer = DictWriter(out_data, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for student in DictReader(in_data):
            last, first = student["name"].split(", ")
            writer.writerow({"first": first,
                             "last": last,
                             "house": student["house"]
                             })


if __name__ == "__main__":
    main()