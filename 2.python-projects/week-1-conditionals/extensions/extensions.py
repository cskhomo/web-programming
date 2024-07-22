import os

def main():

    extensions()

def extensions():

    name = input("File name: ")
    formatted_name =  name.strip().lower()
    base, extension = os.path.splitext(formatted_name)

    match extension:

        case ".jpg" | ".jpeg":
            print("image/jpeg")

        case ".gif":
            print("image/gif")

        case ".png":
            print("image/png")

        case ".pdf":
            print("application/pdf")

        case ".txt":
            print("text/plain")

        case ".zip":
            print("application/zip")

        case _:
            print("application/octet-stream")

main()
