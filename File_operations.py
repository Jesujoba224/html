#create a new file
new_file = open('Codingal.txt', 'x')


new_file.close()


#check if a file exists
import os


print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")


#create a new if it doesn't
my_file = open("Codingal.txt", "w")


my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()


#delete file named codingal
os.remove('Codingal.txt')


#delete the folder
os.rmdir('C:\Users\USER\Desktop\Jesujoba html\PRACTICE HTML\Operation html')