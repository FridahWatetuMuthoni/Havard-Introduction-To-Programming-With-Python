"""
The print function prototype:
print(*objects, sep=' ', end = '\n', file=sys.stdout, flush=false) 
"""


# Examples
username = "Anna"
print("Hello ", end="")
print(username)

print("Hello,", username, sep='_')


def my_func(*objects):

    if (len(objects) > 0):
        for element in objects:
            print(element)


my_func("anna", "jane", "emily", "jackline", "martin")


print("Back\n" * 3, end="")
