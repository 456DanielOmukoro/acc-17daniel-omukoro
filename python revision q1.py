compnum = 50
user=int(input('Please enter a number:'))
count=1

while user!=compnum:
    print('Incorrcet')
    if user>compnum:
        print('Too high')
        count+=1
    elif user<compnum:
        print('Too low')
        count+=1
    else:
        print('Well done it took you',count,'attempts')
 
        break

    user=int(input('Please enter a number'))
    
    
    
        
        
    
        