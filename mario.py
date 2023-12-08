def print_square(size):
    for i in range(size):
        for j in range(size):
            print("# ", end="")
        print()


print_square(4)


def print_xmas(size):
    for i in range(size):
        for j in range(i):
            print("#", end="")
        print()


print_xmas(7)
