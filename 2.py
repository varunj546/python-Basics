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