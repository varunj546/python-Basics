1. Tuples in Python
Explanation:
A tuple is a collection of values stored in a single variable. Tuples are ordered but cannot be changed after they are created. They can store different types of data.
Code:
student = ("Anjali", 20, "AIML", 8.9)

print(student)
print(student[0])
print(student[-1])
2. Accessing Tuple Elements
Explanation:
You can access tuple elements using index numbers or by slicing.
Code:
months = ("January", "February", "March", "April", "May")

print(months[2])
print(months[-2])
print(months[1:4])


3. Tuple Operations
Explanation:
Although tuples cannot be modified, you can join tuples, repeat them, and check if an element exists.
Code:
odd = (1, 3, 5)
even = (2, 4, 6)

numbers = odd + even
print(numbers)

print(("AI", "ML") * 2)

print(4 in numbers)

4. Tuple Methods
Explanation:
Tuples provide methods such as count() to count occurrences and index() to find the position of an element.
Code:
colors = ("Red", "Blue", "Green", "Blue", "Yellow")

print(colors.count("Blue"))
print(colors.index("Green"))

6. Sets in Python
Explanation:
A set is an unordered collection of unique elements. Duplicate values are automatically removed.
Code:
numbers = {10, 20, 30, 20, 40, 10}

print(numbers)

7. Set Operations
Explanation:
Sets support mathematical operations like union, intersection, difference, and symmetric difference.
Code:
A = {2, 4, 6, 8}
B = {6, 8, 10, 12}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)