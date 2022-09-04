import csv
f = open('data.csv','w',newline='')



header = ['firstname','lastname','phone number']
Fname1 = ['Tom','Smith','22344033']
Fname2 = ['Sandra','Jones','22344033']
Fname3 = ['John','Jacob','55007788']



db = csv.writer(f)

db.writerow(header)
db.writerow(Fname1)
db.writerow(Fname2)
db.writerow(Fname3)
f.close()