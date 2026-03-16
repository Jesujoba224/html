# Program to find the longest consecutive 1's in binary representation of a number

# Take input from user
num = int(input("Enter your number: "))

# Convert to binary and remove '0b' prefix
binary = bin(num)[2:]

# Initialize counters
max_count = 0
current_count = 0

# Iterate through each bit in the binary string
for bit in binary:
    if bit == '1':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

# Output the result
print("Longest consecutive 1's length :", max_count)
