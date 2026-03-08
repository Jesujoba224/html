def check_power_of_8(num):
    if num <= 0:
        return False
    while num > 1:
        if num % 8 != 0:
            return False
        num = num // 8
    return True

# Main program
num = int(input("Enter your number: "))
if check_power_of_8(num):
    print(f"Yes  {num} is the power of 8")
else:
    print(f"No {num} is not the power of 8")