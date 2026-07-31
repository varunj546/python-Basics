Basic for Loop
animals = ["Dog", "Cat", "Cow", "Horse"]

for animal in animals:
    print(animal)for animal in animals:
    print(animal)

2. Using range()
for i in range(5, 16):
    print(i)

3. Looping Through a String
word = "PYTHON"

for letter in word:
    print(letter)

4. Nested for Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)
    print()4. Nested for Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)
    print()

5. Using break
numbers = [5, 10, 15, 20, 25]

for num in numbers:
    if num == 20:
        print("Number Found")
        break
    print(num)

6. Using continue
for i in range(1, 11):
    if i == 6:
        continue
    print(i)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

numbers = [45, 78, 12, 99, 34, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

Basic for Loop
animals = ["Dog", "Cat", "Cow", "Horse"]
Basic for Loop
animals = ["Dog", "Cat", "Cow", "Horse"]

for animal in animals:
    print(animal)for animal in animals:
    print(animal)

2. Using range()
for i in range(5, 16):
    print(i)

3. Looping Through a String
word = "PYTHON"
4. Nested for Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)
    print()4. Nested for Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)
    print()
#list
fruits = ["apple", "banana", "cherry",]
print(fruits[0]) #output orange
print(fruits[-1]) #apple
fruits [1] = "orange" # changing a specific element
print(fruits)
fruits.reverse() #reverse the element of the list in place
print(fruits)
fruits.index("apple") 
print(fruits)
fruits.append("orange") #adding element
print(fruits)
fruits.insert(1, "kiwi")  # inserting an element at the specific index
print(fruits) 
fruits.remove("orange") # removing an element
print(fruits)
fruits.pop() # removing the last item
print(fruits)
fruits.pop(0) # removing the first item
print(fruits)
fruits.clear() #removing the all element
print(fruits) 
#list functions and methods
number = [5, 2, 9, 1 ,1, 1] 
print(sorted(number))
print(sum(number)) 
print(number.count(1))
number = [5, 2, 9, 1 ,1, 1] 
number.sort()
print(number)
#nested list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
print(matrix[1:2])
6. Using continue
for i in range(1, 11):
    if i == 6:
        continue
    print(i)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
else:
    print("Second number is greater")
#list
fruits = ["apple", "banana", "cherry",]
print(fruits[0]) #output orange
print(fruits[-1]) #apple
fruits [1] = "orange" # changing a specific element
print(fruits)
fruits.reverse() #reverse the element of the list in place
print(fruits)
fruits.index("apple") 
print(fruits)
fruits.append("orange") #adding element
print(fruits)
fruits.insert(1, "kiwi")  # inserting an element at the specific index
print(fruits) 
fruits.remove("orange") # removing an element
print(fruits)
fruits.pop() # removing the last item
print(fruits)
fruits.pop(0) # removing the first item
print(fruits)
fruits.clear() #removing the all element
print(fruits) 
#list functions and methods
number = [5, 2, 9, 1 ,1, 1] 
print(sorted(number))
print(sum(number)) 
print(number.count(1))
number = [5, 2, 9, 1 ,1, 1] 
number.sort()
print(number)
#nested list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
print(matrix[1:2]) 

#list
fruits = ["apple", "banana", "cherry",]
print(fruits[0]) #output orange
print(fruits[-1]) #apple
fruits [1] = "orange" # changing a specific element
print(fruits)
fruits.reverse() #reverse the element of the list in place
print(fruits)
fruits.index("apple") 
print(fruits)
fruits.append("orange") #adding element
print(fruits)
fruits.insert(1, "kiwi")  # inserting an element at the specific index
print(fruits) 
fruits.remove("orange") # removing an element
print(fruits)
fruits.pop() # removing the last item
print(fruits)
fruits.pop(0) # removing the first item
print(fruits)
fruits.clear() #removing the all element
print(fruits) 
#list functions and methods
number = [5, 2, 9, 1 ,1, 1] 
print(sorted(number))
print(sum(number)) 
print(number.count(1))
number = [5, 2, 9, 1 ,1, 1] 
number.sort()
print(number)
#nested list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
print(matrix[1:2])

#list
fruits = ["apple", "banana", "cherry",]
print(fruits[0]) #output orange
print(fruits[-1]) #apple
fruits [1] = "orange" # changing a specific element
print(fruits)
fruits.reverse() #reverse the element of the list in place
print(fruits)
fruits.index("apple") 
print(fruits)
fruits.append("orange") #adding element
print(fruits)
fruits.insert(1, "kiwi")  # inserting an element at the specific index
print(fruits) 
fruits.remove("orange") # removing an element
print(fruits)
fruits.pop() # removing the last item
print(fruits)
fruits.pop(0) # removing the first item
print(fruits)
fruits.clear() #removing the all element
print(fruits) 
#list functions and methods
number = [5, 2, 9, 1 ,1, 1] 
print(sorted(number))
print(sum(number)) 
print(number.count(1))
number = [5, 2, 9, 1 ,1, 1] 
number.sort()
print(number)
#nested list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
print(matrix[1:2])

#list
fruits = ["apple", "banana", "cherry",]
print(fruits[0]) #output orange
print(fruits[-1]) #apple
fruits [1] = "orange" # changing a specific element
print(fruits)
fruits.reverse() #reverse the element of the list in place
print(fruits)
fruits.index("apple") 
print(fruits)
fruits.append("orange") #adding element
print(fruits)
fruits.insert(1, "kiwi")  # inserting an element at the specific index
print(fruits) 
fruits.remove("orange") # removing an element
print(fruits)
fruits.pop() # removing the last item
print(fruits)
fruits.pop(0) # removing the first item
print(fruits)
fruits.clear() #removing the all element
print(fruits) 
#list functions and methods
number = [5, 2, 9, 1 ,1, 1] 
print(sorted(number))
print(sum(number)) 
print(number.count(1))
number = [5, 2, 9, 1 ,1, 1] 
number.sort()
print(number)
#nested list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
print(matrix[1:2])
#list
fruits = ["apple", "banana", "cherry",]
print(fruits[0]) #output orange
print(fruits[-1]) #apple
fruits [1] = "orange" # changing a specific element
print(fruits)
fruits.reverse() #reverse the element of the list in place
print(fruits)
fruits.index("apple") 
print(fruits)
fruits.append("orange") #adding element
print(fruits)
fruits.insert(1, "kiwi")  # inserting an element at the specific index
print(fruits) 
fruits.remove("orange") # removing an element
print(fruits)
fruits.pop() # removing the last item
print(fruits)
fruits.pop(0) # removing the first item
print(fruits)
fruits.clear() #removing the all element
print(fruits) 
#list functions and methods
number = [5, 2, 9, 1 ,1, 1] 
print(sorted(number))
print(sum(number)) 
print(number.count(1))
number = [5, 2, 9, 1 ,1, 1] 
number.sort()
print(number)
#nested list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
print(matrix[1:2])