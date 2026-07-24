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

6. Using while Loop for User Input
Explanation:
A while loop can repeatedly ask for input until the user enters the correct value.
Code:
password = ""

while password != "python":
    password = input("Enter Password: ")

print("Access Granted")

7. Real-life Example: ATM Balance Check
Explanation:
The loop continues until the account balance becomes zero.
Code:
balance = 3000

while balance > 0:
    print("Current Balance:", balance)
    withdraw = int(input("Enter Amount: "))
    balance -= withdraw

print("Balance is Zero")

8. Nested while Loop
Explanation:
A nested while loop means placing one while loop inside another. It is useful for repeating tasks in rows and columns.
Code:
row = 1

while row <= 3:
    col = 1
    while col <= 4:
        print("*", end=" ")
        col += 1
    print()
    row += 1
Output:
* * * *
* * * *
* * * *

i = 1

while i <= 10:
    print(i)
    i += 1