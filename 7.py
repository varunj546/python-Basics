1. Creating a Dictionary
Explanation:
A dictionary stores data in key-value pairs. Each key is unique and is used to access its corresponding value.
Code:
student = {
    "Name": "Rahul",
    "Age": 21,
    "Course": "AIML"
}

print(student)

2. Accessing Dictionary Elements
Explanation:
Dictionary values can be accessed using their key. You can use square brackets [] or the get() method.
Code:
book = {
    "Title": "Python Basics",
    "Author": "John",
    "Price": 450
}

print(book["Title"])
print(book.get("Author"))
print(book.get("Publisher", "Not Available"))