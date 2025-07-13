# Arithmetic Operators -> +, -, *, /, //, %, **
# // gives integer output without decimal while / gives exact, % gives remainder, ** gives power

# Conditional Operators -> >, <, >=, <=, !=, ==
# != is not equal to
# = is assignment operator

# Logical Operators -> and & or (binary), not (uniary)
# input and output have boolean datatypes
# in a conditional, inputs are numeric and output is boolean

# Bitwise Operators -> & (and), | (or), ^ (xor)

# Right shift (<<) and left shift (>>)

# Bitwise Not (~) -> inverts 1's and 0's

print(32 << 2)
print(100 >> 3)

print(15 & 16)
print(20|30)

print(11|30)

# if, elif, and else

number = int(input("Enter number: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# try something to compare 2 numbers:

num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))

if num_1 > num_2:
    print(num_1, ">", num_2)
elif num_1 == num_2:
    print(num_1, "=", num_2)
else:
     print(num_1, "<", num_2)

# a leap year is classified as a year that is divisible by 4 but not divisible by 100; or divisible by 400

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# check if a number is positive, negative or 0

number = int(input("Enter number: "))

if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")

# let's find the maximum of 3 numbers

num_3 = int(input("Enter number 1: "))
num_4 = int(input("Enter number 2: "))
num_5 = int(input("Enter number 3: "))

if num_3 >= num_4 and num_3 >= num_5:
    print(num_3, "is the greatest")
elif num_4 >= num_5:
    print(num_4, "is the greatest")
else:
    print(num_5, "is the greatest")

# how to figure out if a letter is a vowel or not

letter_1 = input("Enter letter 1: ")

if letter_1 in ["a", "e", "i", "o", "u"]:
    print("letter is a vowel")
else:
    print("letter is not a vowel")

# ASSIGNMENT: Write a program to check last digit of number is divisible by 3 or not

input_number = input("Enter number: ")
last_digit = int(input_number[-1])

if last_digit % 3 == 0:
    print("Last digit is divisible by 3!")
else:
    print("Last digit is not divisible by 3.")
