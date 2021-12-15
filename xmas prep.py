file1 = open('DanielChristmasTest2021.txt', 'w')

#Program 1 list [23,1,0,-12,48]

list1 = [23,1,0,-12,48]
add = 0
for item in list1:
    add = add + item

file1 = open('DanielChristmasTest2021.txt', 'w')
file1.write(str(add))
print(str(add))
file1.close()

    

#program 2 sum of all odd numbers
odd = 0
for item in list1:
    if item %2 != 0:
        odd = odd + item
print(odd)


#program 3 all the even numbers in a list
even = 0
for item in list1:
    if item %2 ==0:
        even += +1
print(even) 
        
        
#multply wiht product by product
        
    
    
    
    