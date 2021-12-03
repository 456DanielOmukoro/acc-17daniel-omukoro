file10 = open('C:/Users/17DOmukoro.ACC/Downloads/10Random.txt', 'r')
file100 = open('C:/Users/17DOmukoro.ACC/Downloads/100Random.txt' , 'r')
'''
min= 100000000000000
max= 0

list2 =[]

for line in file10:
    for item in line.split():
        number = int(item)
        list2.append(number)
        if(number < min):
            min= int(item)
        if(number > max ):
            max= int(item)
range=(max-min)
print(range)


list1 = []
for item in list2:
    if item not in list1:
        list1.append(item)
#frequency = [] 

for item in list1:
   

        #frequency = (line.count(item))
        print (item, 'occurs', list2.count(item), 'times')
        '''


number = 0      
add = 0
mean = []
for line in file10:
    for item in line.split():
        number=(add + int(item))+1
        mean= (number/
    
        
       
        
       # mean = count+1
        
        
    print(number)
    
    
    
    
        



        



