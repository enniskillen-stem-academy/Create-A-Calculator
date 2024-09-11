# Exercise 1: Working with Variables and Data Types
# Instructions: Follow the comments and complete the code.

# 1. Declare a variable 'name' and assign it your name as a string.
name = # Your code here

# 2. Declare a variable 'age' and assign it your age as an integer.
age = # Your code here

# 3. Declare a variable 'height' and assign it your height as a float (e.g., 1.75).
height = # Your code here

# 4. Declare a variable 'is_student' and assign it a boolean value (True or False) depending on whether you are a student.
is_student = # Your code here

# 5. Print out the variables in the following format:
# "My name is <name>, I am <age> years old, and I am <height> meters tall."
print("My name is", name, "I am", age, "years old, and I am", height, "meters tall.")

# 6. Use an if statement to print "I am a student." if 'is_student' is True, otherwise print "I am not a student."
if is_student:
    print("I am a student.")
else:
    print("I am not a student.")

# 7. Use input() to ask the user for their name and age, then print it out in the same format.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name, "you are", age, "years old.")

# 8. Create a new variable 'years_until_100' which calculates how many years until the user turns 100.
years_until_100 = 100 - age
print(name, "will turn 100 in", years_until_100, "years.")

# 9. Experiment: Change the values of 'name', 'age', 'height', and 'is_student' and run the code again.

# 10. Challenge: Add another input() to ask for the user's favorite color and print it in the sentence:
# "Your favorite color is <color>."
color = input("What is your favorite color? ")
print("Your favorite color is", color + ".")

# 11. Advanced Challenge: Add an input to ask for the user's birth year. Calculate their age based on the current year.
birth_year = int(input("Enter your birth year: "))
current_year = 2024
calculated_age = current_year - birth_year
print("You are", calculated_age, "years old.")
