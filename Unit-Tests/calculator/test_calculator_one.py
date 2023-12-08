from calculator import square


def main():
    test_square()


def test_square():
    if (square(2) != 4):
        print("2 squared is not equal to 4")
    if (square(3) != 9):
        print("3 sqaured is not eqaul to 9")


if (__name__ == "__main__"):
    main()
