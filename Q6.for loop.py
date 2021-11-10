#outer loop
rows = int(input('enter rows'))+1


for row in range (rows):
    #nested loop-for each value of i in the outer loop,
    #j will ilerate through all the values from 1 to 10
    for i in range( row): #print multiplication
        print('*',end=' ')
    print()#An empty print statement prints a new line
    
    
