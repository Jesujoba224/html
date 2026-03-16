# Program to find all substrings of a string

# Take input from user
s = input("Enter string : ")

# Generate all substrings
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
