# The fizz buzz program
# Loop thru numbers 0 to n
# check if a number is divisible by 3 if so print fizz
# check if a number is divible by 5 if so print buzzz
# if number is divisible by both 3 and 5 print fizzbuzz
# else print the number itsself

def fizz_buzz(n):
    for element in range(1, n+1):
        str = ""
        if (element % 3 == 0):
            str += 'fizz'
        if (element % 5 == 0):
            str += 'buzz'
        print(str or element)


fizz_buzz(20)
