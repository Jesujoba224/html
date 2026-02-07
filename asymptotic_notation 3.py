def ONSquareTime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end =" ")
            iteration+=1
            print("")
        print("\nWhen n is ",n," Iterations = ",iteration,"\n")
        
ONSquareTime(10)
ONSquareTime(4)
ONSquareTime(3)

print("\nWith every 'n' the time taken equals n^2")
print("0(n^2)")