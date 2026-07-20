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

3. Adding and Updating Dictionary Elements
Explanation:
You can add a new key-value pair or change the value of an existing key.
Code:
employee = {
    "ID": 101,
    "Name": "Priya"
}

employee["Department"] = "HR"
employee["Name"] = "Ananya"

print(employee)

4. Removing Elements from a Dictionary
Explanation:
Dictionary elements can be removed using pop(), del, or clear().
Code:
mobile = {
    "Brand": "Samsung",
    "Model": "A35",
    "Color": "Blue"
}

mobile.pop("Color")
del mobile["Model"]

print(mobile)

mobile.clear()
print(mobile)

5. Dictionary Methods
Explanation:
Dictionary methods help you retrieve keys, values, key-value pairs, and update the dictionary.
Code:
car = {
    "Brand": "Toyota",
    "Model": "Innova",
    "Year": 2024
}

print(car.keys())
print(car.values())
print(car.items())

car.update({"Color": "White"})
print(car)