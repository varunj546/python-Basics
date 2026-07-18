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