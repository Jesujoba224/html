def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print ("AFter Swapping: a =", a, "b =", b)
    
swap(1,2)
    
    
    
    
def swap2(a,b):
        a = (a & b) + (a | b)
        b = a + (~b) + 1
        a = a + (~b) + 1
        print ("After Swapping: a =", a, " b =", b)
        
        
swap2(1,2) 