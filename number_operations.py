""" 
Symbols used with numbers:
+ -> addition
- -> subtraction
* ->multiplication
// -> floor division
/ -> division
% -> modulus
** -> power
"""
num1 = 50
num2 = 12
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
result = x / y
print(result)
print(f"{result:.2f}")  # rounding the result to 2 decimal places

number = 1000
print(f"{number:,}")  # adding a comma after every three digits in a number
