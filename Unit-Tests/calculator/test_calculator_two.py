from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not equal to 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not equal to 9")


if (__name__ == "__main__"):
    main()
