def get_email():
    while True:
        email = input("Enter a valid email: ")
        if (email and "@" in email):
            return email.strip()


def validate_email_one():
    email = get_email()
    if ("@" in email and "." in email):
        print("Success.Email Valid")
        print(f"Email: {email}")
    else:
        print("Invalid Email")


def validate_email():
    email = get_email()
    username, domain = email.split("@")
    if (username and domain.endswith(".edu")):
        print("Email Valid")
    else:
        print("Email Invalid")


validate_email()
