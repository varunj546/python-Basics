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