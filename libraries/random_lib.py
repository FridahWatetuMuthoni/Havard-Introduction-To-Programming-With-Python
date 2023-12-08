import random


# Getting choice from a list/tuple
fruits = ['apple', 'strawberry', 'pineapple', 'kiwi', 'banana']
fruit = random.choice(fruits)
print(fruit)

# Getting a random integer in a given range

random_integer = random.randint(0, 100)
print(random_integer)

# Getting a random color in a list
colors = ['red', 'green', 'purple', 'blue', 'yellow']
random_index = random.randint(0, len(colors)-1)
random_color = colors[random_index]
print(random_color)

# shuffling the list that its given. It shuffles the list in place and does not return anything
numbers = [7, 1, 8, 6, 14, 65, 45, 78, 96, 36, 5, 6]
random.shuffle(numbers)
print(numbers)
