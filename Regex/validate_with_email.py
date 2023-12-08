import re

""" 
For searching patterns:
re.search(pattern, string, flags=0)
re.match(pattern, string, flags=0)
re.fullmatch(pattern, string, flags=0)
re.sub(pattern,repl, string, count=0, flags=0)

re library Bultin Flags:
1. re.IGNORECASE
2. re.MULTILINE
3. re.DOTALL

"""


def get_email():
    while True:
        email = input("Enter a valid email: ")
        if (email and "@" in email):
            return email.strip()


def email_validation_one():
    email = get_email()
    if (re.search(r".+@.+\.edu", email)):
        print("Email Valid")
    else:
        print("Email Invalid")


def email_validation_two():
    email = get_email()
    if (re.search(r"^.+@.+\.edu$", email)):
        print("Email Valid")
    else:
        print("Email Invalid")


def email_validation_three():
    email = get_email()
    if (re.search(r"^[A-Za-z0-9_]+@[A-Za-z0-9]+\.edu$", email)):
        print("Email Valid")
    else:
        print("Email Invalid")


def email_validation_four():
    email = get_email()
    if (re.search(r"^\w+@\w+\.(edu|com|net|gov)$", email, re.IGNORECASE)):
        print("Email Valid")
    else:
        print("Email Invalid")


def email_validation_five():
    email = get_email()
    if (re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|net|gov)$", email, re.IGNORECASE)):
        print("Email Valid")
    else:
        print("Email Invalid")


# email_validation_five()
