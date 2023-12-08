import re


def get_username():
    while True:
        username = input("Please Enter Your Username: ")
        if (username):
            return username.strip()


def validate_username_one():
    username = get_username()
    if ("," in username):
        last, first = username.split(", ")
        name = f"{first} {last}"
        print(name)


def validate_username_two():
    username = get_username()
    matches = re.search(r"^(.+), *(.+)$", username)
    if matches:
        last, first = matches.groups()
        name = f"{first} {last}"
        print(name)


def validate_username():
    username = get_username()
    if matches := re.search(r"^(.+), *(.+)$", username):
        last, first = matches.groups()
        name = f"{first} {last}"
        print(name)


validate_username()
