default_list = ['a', 'b', 'c', 'd']

# Menu
while True:
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
    option =1 
    if user < 0 or user > 9:
        print('Error')

    elif user == 1:
        while option:
        
            

            print('Option 1: Append an Element')
            print()


            user_append = input('Enter the element to be Appended to the List: ')
            print('List before operation:' , default_list)
            default_list.append(user_append)
            print('List after operation: ' , default_list)
        
            option =int(input ('Press 0 to go back to main menu and 1 to repeat action'))
            print()
        
               
            
        

        
        
        
       
    
     
    elif user == 2:
        while option:
            
            
            print('Option 2:Insert an element ')
            print()

            user_insert = input('Enter the element to be inserted')
            print('List before operation: ' , default_list)
            user_location= int(input('Where do you want to insert the element'))
    
            default_list.insert(user_location,user_insert)
            print('List before operation: ' , default_list)
            
            option =int(input ('Press 0 to go back to main menu and 1 to repeat action'))
            print()
            
            
            
     elif user == :
         while option:
             print('Option 3:Append a list to the given list')
             print()
             
             
    

