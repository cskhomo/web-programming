def main():

    months = {
                "January" : 1, "February" : 2, "March" : 3,
                "April" : 4, "May" : 5, "June" : 6,
                "July" : 7, "August" : 8, "September" : 9,
                "October" : 10, "November" : 11, "December" : 12,
            }

    while True:

        date = input("Date: ")

        try:
            m, d, y = date.split("/")
            mm, dd, yyyy = int(m), int(d), int(y)

        except:

            try:
                md, y = date.split(",")
                m, d = md.split(" ")
                mm, dd, yyyy = months[m], int(d), int(y)

            except: continue

            else:
                if dd < 32:
                    break

        else:
            if mm < 13 and dd < 32:
                break

    print(f"{yyyy}-{mm:02}-{dd:02}")


main()
