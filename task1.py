# Program to add two numbers

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating the sum
sum_result = num1 + num2

# Displaying the result
print("The sum of", num1, "and", num2, "is:", sum_result)


# Odd or Even Checker

# Taking input from the user
num = int(input("Enter a number to check it is odd/even: "))

# Checking if the number is even or odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# Factorial using a loop

num = int(input("Enter a number for factorial: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is:", factorial)


# Fibonacci sequence using a loop

n = int(input("Enter the number of terms: "))

a, b = 0, 1
sequence = []

if n <= 0:
    print("Please enter a positive integer.")
else:
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence up to", n, "terms:")
    print(sequence)


# String Reverse Program

# Taking input from the user
text = input("Enter a string for reverse: ")

# Reversing the string using slicing
reversed_text = text[::-1]

# Displaying the result
print("Reversed string:", reversed_text)

# Palindrome Checker

# Taking input from the user
word = input("Enter a word is palindrome or not : ")

# Reversing the word
reversed_word = word[::-1]

# Checking if the word is a palindrome
if word == reversed_word:
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")

    # Leap Year Checker

year = int(input("Enter a year to check a leap year : "))

# Leap year conditions:
# 1. Divisible by 4
# 2. Not divisible by 100, unless also divisible by 400

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")


# Armstrong Number Checker

num = int(input("Enter a number to check it is armstrong or not : "))

# Convert number to string to count digits
num_str = str(num)
num_len = len(num_str)

# Calculate sum of digits raised to the power of number of digits
sum_of_powers = sum(int(digit) ** num_len for digit in num_str)

# Check if Armstrong number
if num == sum_of_powers:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")


