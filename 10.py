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
