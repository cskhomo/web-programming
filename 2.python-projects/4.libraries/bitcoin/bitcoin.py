import requests
import sys

def main():

    try: coins = float(sys.argv[1])

    except(IndexError): sys.exit("Missing command-line argument")

    except(ValueError): sys.exit("Command-line argument is not a number")

    else:
        rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
        price = coins * rate
        print(f"${str(price)[:2]},{str(price)[2:]}")

main()
