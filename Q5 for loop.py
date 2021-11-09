#outer loop
for i in range(1, 11):
    #nested loop-for each value of i in the outer loop,
    #j will ilerate through all the values from 1 to 10
    for j in range(1, 11): #print multiplication
        print(i*j,end=' ')
    print() #An empty print statement prints a new line
    