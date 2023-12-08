# Strings Functions and Manipulation

# Removing white spaces from strings
white_space = " Hello, World    "
print(white_space)
print(white_space.strip())

# capitalizing strings
capitalize_name = "david malan"
print(capitalize_name.capitalize())

# Title bases capitalization
title_name = "David malan"
print(title_name.title())

# String to lowercase
str_lowercase = "AnNa"
print(str_lowercase.lower())

# string to uppercase
str_uppercase = "amy"
print(str_uppercase.upper())

# Replacing words in a string

replacing_string = "Help you"
print(replacing_string.replace("you", "me"))

# slipting a string to an array
string_spliting = "Hello, we are learning python programming"
string_arr = string_spliting.split(" ")
print(string_arr)

str_spliting = "Hanna, Amy, jane, Mary"
str_arr = str_spliting.split(",")
print(str_arr)

full_name = "Fridah Watetu"
first, last = full_name.split(" ")
print(f"First Name: {first}, Last Name: {last}")

# Finding if a string starts with a certain letter or word
sentence = "Need to start a fire and cook the rice"

print(sentence.startswith('Need'))
print(sentence.startswith('N'))

# Finding if a string ends with a certain word or letter
print(sentence.endswith("rice"))
print(sentence.endswith('e'))

# Find the index of the first occurence of a letter in a string
letter_index = "Bye Bye"
print(letter_index.index('e'))

# Returns the index of the first occurence of a letter
letter_find = "Oh hi there"
print(letter_find.find("i"))

# Counting the number of a certain letter in a sentence
how_many_e = "Bye Bye"
print(how_many_e.count('e'))

# STRING FORMATTING
name = "Janeffer Lopez"
print(name[4])
print(name[:])
print(name[1:])
print(name[:1])
print(name[-1])
print(name[::1])
print(name[::-1])
print(name[0:10:1])
