'''
L = [1,2,3,4,5,6,7]
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(7))
'''

List = 1234567

def addList(L):
    if L<10:
        return L
    else:
        return L % 10 +addList(L//10)
print(addList(List))   