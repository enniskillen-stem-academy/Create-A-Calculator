# Exercise 2: User Input, Strings, and Basic Math Operations
# Instructions: Follow the comments and complete the code.

# 1. Ask the user to enter their first name and store it in a variable 'first_name'.
first_name = input("Enter your first name: ")

# 2. Ask the user to enter their last name and store it in a variable 'last_name'.
last_name = input("Enter your last name: ")

# 3. Print out the full name in the format: "Hello, <first_name> <last_name>!".
print("Hello,", first_name, last_name + "!")

# 4. Ask the user to enter their age and store it in a variable 'age' as an integer.
age = int(input("Enter your age: "))

# 5. Print a message saying how old they will be in 5 years.
age_in_5_years = age + 5
print("In 5 years, you will be", age_in_5_years, "years old.")

# 6. Ask the user to enter a number and store it in a variable 'number'.
number = int(input("Enter a number: "))

# 7. Print the square of the number (number * number).
print("The square of", number, "is", number * number)

# 8. Ask the user for two numbers, store them in variables, and print their sum.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_of_numbers = num1 + num2
print("The sum of", num1, "and", num2, "is", sum_of_numbers)

# 9. Ask the user for a favorite word and store it in 'favorite_word'.
favorite_word = input("What is your favorite word? ")

# 10. Print the favorite word in uppercase and lowercase.
print("Your favorite word in uppercase is:", favorite_word.upper())
print("Your favorite word in lowercase is:", favorite_word.lower())

# 11. Challenge: Ask the user for a sentence and count how many words are in the sentence.
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("Your sentence contains", word_count, "words.")
