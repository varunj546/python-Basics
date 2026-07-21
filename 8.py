1. The if Statement
Explanation:
The if statement checks whether a condition is True. If it is, the code inside the if block is executed.
Code:
temperature = 32

if temperature > 30:
    print("The weather is hot.")
2. The else Statement
Explanation:
The else statement runs when the if condition is False.
Code:
password = "python123"

if password == "admin123":
    print("Login Successful")
else:
    print("Invalid Password")

The elif Statement
Explanation:
The elif statement is used to check multiple conditions one after another. If one condition is true, the remaining conditions are skipped.
Code:
score = 72

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 50:
    print("Good")
else:
    print("Needs Improvement")

4. Comparison Operators in if Statements
Explanation:
Comparison operators compare two values and return either True or False.
Code:
balance = 5000

if balance > 3000:
    print("You have sufficient balance.")
else:
    print("Low balance.")

5. Logical Operators in if Statements
Explanation:
Logical operators (and, or, not) combine two or more conditions.
Code:
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Login Failed")

6. Example: Checking Electricity Bill Discount
Explanation:
The discount depends on the total electricity bill amount.
Code:
bill = 1800

if bill >= 3000:
    print("20% Discount")
elif bill >= 2000:
    print("10% Discount")
elif bill >= 1000:
    print("5% Discount")
else:
    print("No Discount")

7. Nested if Statements
Explanation:
A nested if means placing one if statement inside another if statement.
Code:
has_ticket = True
has_id = True

if has_ticket:
    if has_id:
        print("Entry Allowed")
    else:
        print("Show your ID Card")
else:
    print("Please Buy a Ticket")

8. Indentation in Python
Explanation:
Python uses indentation (spaces) to define which statements belong to an if, elif, or else block. Incorrect indentation causes an error.
Code:
age = 22

if age >= 18:
    print("Eligible for Driving License")
    print("Drive Safely")
else:
    print("Not Eligible")

9. The match-case Statement (Python 3.10+)
Explanation:
The match-case statement checks a variable against multiple values. It is similar to the switch-case statement in other programming languages.
Code:
fruit = "Apple"

match fruit:
    case "Apple":
        print("Apple is Red.")
    case "Banana":
        print("Banana is Yellow.")
    case "Orange":
        print("Orange is Orange.")
    case _:
        print("Fruit Not Found")