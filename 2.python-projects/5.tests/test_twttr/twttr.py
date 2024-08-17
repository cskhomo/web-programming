def main():

    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):

    vowels = "aeiouAEIOU"
    tweet = str()

    for alpha in word:
        if alpha not in vowels:
            tweet += alpha

    return tweet

if __name__ == "__main__":
    main()