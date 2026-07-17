1. Assignment Operators
Explanation:
Assignment operators are used to store a value in a variable or update the value after performing an operation.
Code:
marks = 50
print("Initial Marks:", marks)

marks += 20
print("After Adding:", marks)

marks -= 10
print("After Subtracting:", marks)

marks *= 2
print("After Multiplying:", marks)

marks %= 15
print("Remainder:", marks)

2. Comparison Operators
Explanation:
Comparison operators compare two values and return True if the condition is correct, otherwise False.
Code:
height1 = 165
height2 = 170

print(height1 == height2)
print(height1 != height2)
print(height1 > height2)
print(height1 < height2)
print(height1 >= 165)
print(height2 <= 180)

3. Logical Operators
Explanation:
Logical operators are used to combine multiple conditions in one statement.
Code:
english = 65
maths = 80

print(english >= 35 and maths >= 35)
print(english >= 70 or maths >= 70)
print(not english < 35)

4. Membership Operators
Explanation:
Membership operators check whether a value is present or absent in a list, tuple, or string.
Code:
colors = ["Red", "Blue", "Green", "Black"]

print("Blue" in colors)
print("White" in colors)
print("Yellow" not in colors)
print("Green" not in colors)


5. Bitwise Operators
Explanation:
Bitwise operators perform operations on the binary form (0s and 1s) of numbers.
Code:
a = 9
b = 6

print("AND =", a & b)
print("OR =", a | b)
print("XOR =", a ^ b)
print("NOT =", ~a)
print("Left Shift =", a << 1)
print("Right Shift =", b >> 1)

6. Arithmetic Operators
Explanation:
Arithmetic operators are used to perform basic mathematical calculations such as addition, subtraction, multiplication, division, remainder, and exponentiation.
Code:
length = 12
width = 5

print("Addition =", length + width)
print("Subtraction =", length - width)
print("Multiplication =", length * width)
print("Division =", length / width)
print("Floor Division =", length // width)
print("Modulus =", length % width)
print("Power =", length ** 2)