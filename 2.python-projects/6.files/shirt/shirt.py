from sys import argv, exit
from PIL import Image, ImageOps


def main():
    file_status = check_args(argv)
    
    if file_status.startswith("!"):
        exit(file_status.strip("!"))

    try:
        add_shirt(argv)
    except FileNotFoundError:
        exit("Input does not exist")


def add_shirt(argv):
    selfie = Image.open(argv[1])
    shirt = Image.open("shirt.png")
    selfie = ImageOps.fit(selfie, shirt.size)
    selfie.paste(shirt, shirt)
    selfie.save(argv[2])


def check_args(argv):
    if len(argv) < 3:
        return "!Too few command-line arguments"

    if len(argv) > 3:
        return "!Too many command-line arguments"

    in_file = argv[1]
    out_file = argv[2]

    if not out_file.lower().endswith((".jpg", ".jpeg", ".png")):
        return "!Invalid output"

    if in_file.lower()[-3:] != out_file.lower()[-3:]:
        return "!Input and output have different extensions"
    
    return "Valid arguments"


if __name__ == "__main__":
    main()