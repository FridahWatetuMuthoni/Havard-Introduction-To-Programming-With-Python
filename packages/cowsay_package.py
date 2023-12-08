# installing cowsay: pip install cowsay
import cowsay
import sys


def cowsay_name():
    if (len(sys.argv) == 2):
        cowsay.cow(f"Hello, {sys.argv[1]}")
        cowsay.trex(f"Hello, {sys.argv[1]}")
    else:
        print("You didnt provide a name")

# cowsay_name()


def cowsay_cow():
    name = "Emily"
    cowsay.cow(f"Hello, {name}")


cowsay_cow()


def cowsay_trex():
    name = "Anna"
    cowsay.trex(f"Hello, {name}")


cowsay_trex()
