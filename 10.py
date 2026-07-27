Basic for Loop
animals = ["Dog", "Cat", "Cow", "Horse"]

for animal in animals:
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