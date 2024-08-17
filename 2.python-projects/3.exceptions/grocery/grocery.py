def main():

    groceryDict = dict()
    groceryList = list()

    while True:

        try:
            item = input().upper()

        except EOFError:
            break

        else:
            if item in groceryDict:
                groceryDict[item] += 1
            else:
                groceryDict[item] = 1
                groceryList.append(item)

    groceryList = sorted(groceryList)

    for item in groceryList:
        print(groceryDict[item], item)

main()
