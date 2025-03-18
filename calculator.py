#Prompt the user to input two numbers and mathematical operation
x1=float(input("Input the first number: "))
x2=float(input("Input the second number: "))
mo=input("Choose mathematical operation to use (+, -, * or /): " )

if mo == "+":
    print("Your result is ", str(x1), "+", str(x2), "=", str(x1 + x2))
elif mo == "-":
    print("Your result is ", str(x1), "-", str(x2), "=", str(x1 - x2))
elif mo == "*":
    print("Your result is ", str(x1), "*", str(x2), "=", str(x1 * x2))
elif mo == "/":
    while True:
        if x2 == 0:
            print("Division by zero is not possible, please select another number.")
            x2 = float(input("Input the second number: "))
        else:
            break
    print("Your result is ", str(x1), "/", str(x2), "=", str(x1 / x2))