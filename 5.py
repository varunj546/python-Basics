1. What is a List?
A list is a collection of multiple values stored in a single variable. Lists are ordered, changeable (mutable), and can contain duplicate values and different data types.
Code:
student = ["Rahul", 21, "AIML", True]
print(student)


2. Accessing List Elements
Explanation:
You can access list elements using their index number. The first element starts at index 0, and negative indexing starts from the last element.
Code:
cities = ["Mangalore", "Bangalore", "Mysore", "Hubli"]

print(cities[1])
print(cities[3])
print(cities[-1])
print(cities[-2])

3. Modifying Lists
Explanation:
Since lists are mutable, you can change, add, or remove elements after creating the list.
Code:
languages = ["Python", "Java", "C"]

languages[2] = "C++"
languages.append("HTML")
languages.insert(1, "JavaScript")
languages.remove("Java")
languages.pop()

print(languages)

4. Slicing Lists
Explanation:
Slicing is used to extract a portion of a list. It allows you to select a range of elements.
Code:
marks = [45, 56, 67, 78, 89, 91, 95]

print(marks[2:6])
print(marks[:5])
print(marks[3:])
print(marks[1:7:2])


5. List Functions and Methods
Explanation:
Python provides built-in functions and methods to perform operations like finding length, sorting, reversing, counting, and locating elements.
Code:
numbers = [18, 7, 25, 12, 7]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))
print("Index of 25:", numbers.index(25))
print("Count of 7:", numbers.count(7))

numbers.reverse()
print("Reversed:", numbers)

numbers.sort()
print("Sorted List:", numbers)

6. Nested Lists
Explanation:
A nested list is a list that contains one or more lists as its elements. It is useful for storing data in rows and columns.
Code:
employees = [
    ["Ravi", 101, "HR"],
    ["Anu", 102, "Finance"],
    ["Kiran", 103, "IT"]
]

print(employees[0])
print(employees[2][0])
print(employees[1][2])