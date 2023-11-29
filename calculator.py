print("The operator are :\n\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n")
op = int(input("Enter the option : "))
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second numbers : "))
if (op == 1):
    print("The Addition is ", num1+num2)
elif (op == 2):
    print("The Substraction  is ", num1-num2)
elif (op == 3):
    print("The Multiplication is ", num1*num2)
elif (op == 4):
    print("The Division is ", num1/num2)
else:
    print("Invalid Operator")
