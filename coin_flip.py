import random


def flip():

    flip = random.random()
    if flip >= .5:
        return True
    else:
        return False


def main(num):
    heads = 0
    tails = 0
    resString = ""

    for i in range(int(num)):
        if flip():
            heads += 1
            resString += "Head\n"
        else:
            tails += 1
            resString += "Tail\n"

        print("Number of Heads: %i" % (heads))
        print("Number of Tails: %i" % (tails))
        print(resString)


userInput = input("Please enter a number of flips: ")
main(userInput)
