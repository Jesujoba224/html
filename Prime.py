from math import sqrt
number = int(input("number to check prime :" ))
for k in range(2, int(sqrt(number))+1):
    if (number % k) ==0:
        print(number, "is not a prime number")
        break
else:
    print(number, "is a prime number")