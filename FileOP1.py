a = open('Codingal.txt', "r" )
print(a.read())
a.close()

b = open('Codingal.txt', "w" )
b.write("I am learning file operations in Python.")
b.close() 

c = open('Codingal.txt', "a" )
c.write("I am learning Python.")
c.close()