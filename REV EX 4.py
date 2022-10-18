Alphabet=['A','B','C','D','E',F','G','H','I','J','K',L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

chipherlis=[]

chipherlis.append(Alphabet)
chipherlis.append(alphabet)

user=input('Enter a word please')
usershift=int(input('How many letters would you like to shift'))
#DOOR
for line in user:
    location = chipherlis.index(line)
    newlocation = location + usershift
    print(chipherlis[newlocation])