7. Input and Output in Python
7.1 Taking Input from the User
Explanation
The input() function allows the user to enter information while the program is running. Whatever the user types is stored as a string by default. If you need a number, convert it using int() or float().
Example
student = input("Enter your name: ")
semester = int(input("Enter your semester: "))

print(student)
print(semester)

7.2 Displaying Output
Explanation
The print() function displays information on the screen. You can print text, variables, or use f-strings to create readable output.
Example
course = "Artificial Intelligence"
year = 3

print(f"I am studying {course}.")
print(f"I am in {year}rd year.")

8. String Manipulation
8.1 Joining and Repeating Strings
Explanation
You can join strings using the + operator and repeat them using the * operator.
Example
college = "Srinivas"
city = "Mangalore"

print(college + " " + city)

print("Python " * 4)

8.2 Useful String Methods
Explanation
Python provides built-in methods to modify strings without changing the original string.
Example
text = "  artificial intelligence  "

print(text.strip())
print(text.title())
print(text.upper())
print(text.replace("intelligence", "engineering"))
8.3 Accessing Characters
Explanation
Each character in a string has an index number. Positive indexing starts from the beginning, while negative indexing starts from the end.
Example
language = "Programming"

print(language[1])
print(language[5])
print(language[-2])

8.4 String Slicing
Explanation
Slicing extracts a specific part of a string by giving the starting and ending index.
Example
subject = "Machine Learning"

print(subject[0:7])
print(subject[8:])
print(subject[-8:])

9. Comments in Python
Explanation
Comments are notes written inside a program to explain the code. They are ignored when the program runs.
Single-line Comment
# Display student details

print("Welcome to Python")
Multi-line Comment
"""
This program
demonstrates
comments in Python.
"""

print("Learning Python")

