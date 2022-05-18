#(spaces)
f = open("revison.txt","r")
space=0
num=0

counter=0
for line in f:
    for i in line:
        if i == ' ':
            space+=1

print('The file contains',space,'amount of spaces')
f.close()
#(caps)
f = open("revison.txt","r")
words=0
num=0
capitals=0
for line in f:
    for i in line:
        if i.isupper():
            capitals+=1
print('The file contains',capitals,'amount of caps')            
f.close()
#(number)

f = open("revison.txt","r")

num=0
counter=0
for line in f:
    for i in line:
        if i.isdigit():
            num+=1
            

print('The file contains',num,'amount of numbers')
f.close()
#(words)
f = open("revison.txt","r")
word=0
num=0
counter=0
for line in f:
    word+=len(line.split())
    

print('The file contains',word,'amount of words')







