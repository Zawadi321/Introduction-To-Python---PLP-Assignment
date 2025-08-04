#User input
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
Operation = input("Enter operation (+, -, *, /): ")

#addition
if Operation == '+':
    Addition = num1 + num2
    print(num1, "+", num2, "=", Addition)

#subtraction
if Operation == '-':
    Subtraction = num1 - num2
    print(num1, "-", num2, "=", Subtraction)

#multiplication
if Operation == '*':
    Multiplication = num1 * num2
    print(num1, "*", num2, "=", Multiplication)

#division
if  Operation == '/' and num2 != 0:
        Division = num1 / num2
        print(num1, "/", num2, "=", Division)


