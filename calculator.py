num1 = int(input("Enter first number :"))
operator = input("Enter operator :")
num2 = int(input("Enter second number :"))

if operator == "+":
    print(num1+num2)
if operator == "-":
    print(num1-num2)
if operator == "*":
    print(num1*num2)
if operator == "/":
    if num2 == 0:
        print("Cannot divide")
    else:
        print(num1/num2)
