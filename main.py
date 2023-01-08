print("Select an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = int(input())
if operation == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("enter second number: "))
    total = num1 + num2
    print(" your total is " + str(total))
elif operation == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("enter second number: "))
    total = num1 - num2
    print(" your total is " + str(total))
elif operation == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("enter second number: "))
    total = num1 * num2
    print(" your total is " + str(total))
elif operation == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("enter second number: "))
    total = num1 / num2
    print(" your total is " + str(total))
else:
    print(" Invalid operation input")