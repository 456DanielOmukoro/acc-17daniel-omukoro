'''
radius=int(input('What is the radius of a cylinder'))
depth=int(input('What is the depth of a cylinder'))

area=3.141592*radius*(radius)
print (area)

volume=(area*depth)
rounded=round(volume,3)
print(rounded)

'''
user=int(input('''
1.Square
2.Triangle:'''))


if user==1:
    L=int(input('What is the length of the side:'))

    area=L**2
    print(area)
    
elif user==2:
    R=int(input('What is the base of the Triangle:'))
    R=int(input('What is the height of the Triangle:'))
    
    area=R**2
    print(area)
    
else:
    print('Error')

    
