f = open('data.csv','a','\n')



header = ['firstname','lastname','phone number']
body = ['Tom','Smith','22344033','\n','Sandra','Jones','22344033','\n','John','Jacob','55007788']
Fname1 = ['Tom','Smith','22344033']
Fname2 = ['Sandra','Jones','22344033']
Fname3 = ['John','Jacob','55007788']



db = data.writer(f)
db.writewrow(header)
db.writerow(Fname1)
db.writerow(Fname2)
db.writerow(Fname3)
f.close()