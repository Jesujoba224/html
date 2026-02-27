# Program to find the number of bits present in a number
 
# Functions taking our number as input 
def numberOfBits(n):
    
    # Count variable set as 0 
    count = 0
 
    # Right shift the number till it becomes 0
    while (n):
        count += 1
        n >>= 1
         
    return count
 
 
number = int(input("Enter your number : "))
print("Total bits : ",numberOfBits(number))
