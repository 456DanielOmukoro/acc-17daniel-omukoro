Default_list = ['a', 'b', 'c', 'd']
Box = 1
Board = 0
# Menu
while Box > Board:
    print('''
1. Append an element
2. Insert an element
3. Append a list to the given list
4. Modify an existing element
5. Delete an existing element from its position
6. Delete an existing element with a given value
7. Sort the list in the ascending order
8. Sort the list in descending order
9. Display the list. 
''')



user = int(input('Enter Your Choice From 1-9: '))
print()

if user < 0 or user > 9:
    print('Error')

elif user == 1:
    
    print('Option 1: Append an Element')
    print()


    user_append = input('Enter the element to be Appended to the List: ')
    print('List before operation:' , Default_list)
    Default_list.append(user_append)
    print('List after operation: ' , Default_list)
    
   ''' 
elif user == 2:
    print('Option 2:Insert an element ')
    print()
    
    user_insert = input('Enter the element to be inserted')
    print('List before operation: ' , Default_list)
    Default_list.insert(user_insert,Default_list)
    print('List before operation: ' , Default_list)
    
 
    
    
    
    
    
    
    
    
    