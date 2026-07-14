1. Variables in Python
city = "Mangalore"
temperature = 31
is_raining = False

print(city)
print(temperature)
print(is_raining)

2. Data Types in Python
Explanation
A data type tells Python what kind of value is stored in a variable.
int → Whole numbers
float → Decimal numbers
str → Text
bool → True or False
Example
marks = 95
height = 5.4
college = "Srinivas University"
passed = True

print(type(marks))
print(type(height))
print(type(college))
print(type(passed))

3. Type Conversion
Explanation
Sometimes you need to change one data type into another. This process is called type conversion.
Example
price = "250"

price_int = int(price)
discount = float(price_int)

print(price_int)
print(discount)

4. Arithmetic Operators
Explanation
Arithmetic operators are used to perform mathematical calculations.
Example
num1 = 18
num2 = 4

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Remainder:", num1 % num2)
print("Power:", num1 ** num2)

5. Assigning Values to Multiple Variables
Explanation
Python allows you to assign values to multiple variables in one line, making your code shorter and cleaner.
Example 1
fruit, color, quantity = "Apple", "Red", 12

print(fruit)
print(color)
print(quantity)

6. Variable Reassignment
Explanation
The value stored in a variable can be changed at any time. This is called variable reassignment.
Example
status = "Offline"
print(status)

status = "Online"
print(status)