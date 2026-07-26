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

num = 2

while num <= 20:
    print(num)
    num += 2

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)

num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

num_students = int(input("Enter the number of students: "))

students = []

for i in range(num_students):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    marks = []
    total = 0

    for j in range(5):
        mark = int(input("Enter mark for Subject " + str(j + 1) + ": "))
        marks.append(mark)
        total += mark

    average = total / 5
     if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    students.append([name, marks, total, average, grade])

print("\n----- Student Report -----")

for student in students:
    print("Name:", student[0])
    print("Marks:", student[1])
    print("Total:", student[2])
    print("Average:", student[3])
    print("Grade:", student[4])
    print()

balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Please collect your cash")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You for Using ATM")
        break

    else:
        print("Invalid Choice")

employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    name = input("Enter Name: ")
    basic = float(input("Enter Basic Salary: "))

    hra = basic * 0.20
    da = basic * 0.15
    tax = basic * 0.10

    net_salary = basic + hra + da - tax

    employees.append([name, basic, hra, da, tax, net_salary])

print("\n------ Employee Details ------")

for emp in employees:
    print("Name:", emp[0])
    print("Basic Salary:", emp[1])
    print("HRA:", emp[2])
    print("DA:", emp[3])
    print("Tax:", emp[4])
    print("Net Salary:", emp[5])

cart = []
grand_total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    total = price * quantity
    grand_total += total

    cart.append([name, price, quantity, total])

print("\n======= BILL =======")

for item in cart:
    print("Product:", item[0])
    print("Price:", item[1])
    print("Quantity:", item[2])
    print("Total:", item[3])
    print()

print("Grand Total:", grand_total)

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter Number: "))
    numbers.append(num)

positive = 0
negative = 0
even = 0
odd = 0
total = 0

for num in numbers:
    total += num

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

average = total / len(numbers)

print("\n------ Analysis ------")
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)
print("Positive Numbers:", positive)
print("Negative Numbers:", negative)
print("Even Numbers:", even)
print("Odd Numbers:", odd)

for num in numbers:
    total += num
