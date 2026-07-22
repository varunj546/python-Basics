1. Basic while Loop
Explanation:
A while loop repeats a block of code until the condition becomes False.
Code:
count = 1

while count <= 5:
    print("Welcome")
    count += 1
2. Example: Printing Even Numbers
Explanation:
The loop prints only even numbers from 2 to 10.
Code:
num = 2

while num <= 10:
    print(num)
    num += 2

3. Avoiding Infinite Loops
Explanation:
Always update the loop variable. Otherwise, the condition never becomes False and the loop runs forever.
Code:
number = 1

while number <= 3:
    print(number)
    number += 1
4. Using break
Explanation:
The break statement immediately stops the loop when a specific condition is met.
Code:
num = 1

while num <= 10:
    if num == 7:
        print("Loop Stopped")
        break
    print(num)
    num += 1