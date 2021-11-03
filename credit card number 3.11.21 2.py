number = int(input('Enter a Number'))
odddigit = 0
evendigit = 0



while number>0:
    odddigit = odddigit+number%10
    number = number//10
    #evendigit = evendigit+(number%10)*2
    #number = number//10
    evenNumber = number%10*2
    if(evenNumber>9):
            while(evenNumber>0):
                evendigit = evendigit + evenNumber%10
                evenNumber = evenNumber//10
                
    else:
        evendigit = evendigit+evenNumber
    
    
total = odddigit+evendigit
if total%10==0:
    print('valid')

else:
    print('invalid')