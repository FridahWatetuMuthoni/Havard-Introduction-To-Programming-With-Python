def main():
    number = 10
    if (is_even(number)):
        print("Even")
    else:
        print("Odd")


def is_even(number):
    if (number % 2 == 0):
        return True
    return False


def is_even_2(number):
    return True if number % 2 == 0 else False


def is_even_3(number):
    return (number % 2 == 0)


if (__name__ == "__main__"):
    main()
