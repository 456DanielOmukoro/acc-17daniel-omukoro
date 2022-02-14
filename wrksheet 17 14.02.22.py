'''
#1
print('Hello World')
 
 #2
user=input('Please Enter Your Name:')
#print ('Hello', user)
#3
if user == 'Alice' or user== 'Bob':
    print('Hello',user)
else:
    print('Cannot find name')
 #4  
counter=0
n= int(input('Please enter a number')) 
for i in range(1,n+1):
    counter=counter+i
print(counter)
#5
counter=0
n= int(input('Please enter a number')) 
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        counter=counter+i
print(counter)
#6
counter=0
choose=0
product=0
count=1
n=int(input('Enter a number:'))
choose=input('Do you want to compute the sum or the product:')
if choose=='Sum' or choose=='sum':
    print('You are now computing the sum')
    for i in range(1,n+1):
    
            counter=counter+i
            print(counter)
else:
    if choose=='Product' or choose=='product':
        print('You are now computing the product')
        for i in range(1,n+1):
        
            count=count*i
        
    print(count)
#7    
   
for i in range(0,13):
    print(i,'X12','=',i*12)


#8
prime=[2]
isprime=True
for i in range(3,101,1):
    for p in prime:
        if i%p==0:
            isprime=False
    if isprime==True:
        prime.append(i)
    else:
        isprime=True
print(prime)

#9

import random
randomNumber = random.randint(1,10 + 1)

boolean = True
counter = 0
guessList = []

guess = int(input('Enter number between 1 - 10: '))
counter += 1

while boolean:
    if guess == randomNumber:
        print('\nCorrect!!!')
        print('You Guessed', counter, 'Times!')
        boolean = False
        counter += 1
        
    if guess != randomNumber:
        print('Wrong ! Try Again')
        if guess not in guessList:
            counter += 1
            guessList.append(guess)
        guess = int(input('Enter Another Number: '))
'''

#10
counter=0
year=int(input('Please enter the current year'))
for year in range (2000,2400):
    if year%4==0 and 


