#empty tuple
my_tuple=()
print(my_tuple)

#tuple with different data types
my_tuple=(1, "mango", (1,"banana"), {"name": "mango"},[1,2,3] )
print(my_tuple)

#tuple with single element
my_tuple2=(1,4)
print(my_tuple2)

#tuple without parenthesis
my_tuple3=1,2,3,4
print(my_tuple3)

#slicing tuple
my_tuple4=(0,1,2,3,4,5,6,7,8,9)
print(my_tuple4[2:8:2])

#indexing tuple
my_tuple5=("apple", "banana", "cherry", "date")
print(my_tuple5[1])

#nested tuple
my_tuple6=(1, "mango", (1,"banana"), {"name": "mango"},[1,2,3] )
print(my_tuple6)
print(my_tuple6[2]) 

# accessing nested tuple
for letter in (my_tuple7:=("Hello ", "world!")):
    print(letter)