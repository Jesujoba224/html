def checkIfSame(number1, number2):
    if ((number1 ^ number2) != 0):
        print("Numbers are not equal")
    else: 
        print("Both numbers are equal")
        
num1 = int(input("Enter first number to compare : "))
num2 = int(input("Enter second number to compare : "))

checkIfSame(num1, num2)