# my_mod.py


def enlarge(n):
    return n*100


if __name__ == "__main__":
    # only run the code below if running from the command line
    x = 5
    print(enlarge(x))

    y = int(input("Please chooses a number (eg 5): "))
    print(enlarge(y))