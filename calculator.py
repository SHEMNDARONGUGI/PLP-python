num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
operation = input("Input the arithmetic operation to be carried out '+, - ,/,*' ")

if operation == "+":
    result = float(num1) + float(num2)
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = float(num1) - float(num2)
    print(f"{num1} - {num2} = {result}")
elif operation == "/":
    result = float(num1) / float(num2)
    print(f"{num1} / {num2} = {result}")
elif operation == "*":
    result = float(num1) * float(num2)
    print(f"{num1} * {num2} = {result}")
else:
    print("Invalid operation")