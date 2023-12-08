# Get username from user
username = input("What is your name: ")

if (username):
    print(f"Hello, {username}")

else:
    print("Please enter your name")

# Get a number from the user

postive_number = input("Enter a postive number: ")
postive_number = int(postive_number)

result = 10

if (postive_number > 0):
    result += postive_number
    print(result)
else:
    print("Please enter a postive number")
