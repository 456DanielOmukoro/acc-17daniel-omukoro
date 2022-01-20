# Bubble Sort v3
myList = [5, 7, 3, 6, 2, 4, 1]

def bubble_sort(L, descending = False, dbg = True):
    print("INPUT (initial list): ", L)
    exchange = True
    n = len(L)
    i = 0
    while (i < n) and exchange:     
     exchange = False
     for j in range(n-i-1):

        if descending == False:
            if L[j] > L[j+1]:
                 L[j], L[j+1] = L[j+1], L[j]
                 exchange = True         
        elif descending == True:
            if L[j] < L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    exchange = True     
         
     if dbg == True:
         print('Debug Info')
         print("BEFORE PASS %d: %s " %(i+1, L)) 
         print("%s " %L, end="-> ")  
         print("%s " %L)
         print("AFTER PASS %d: %s " %(i+1, L))     
     elif dbg == False:
         ('')
         
     i = i+1
    return(L) #(OUTPUT (sorted list): , L)
result = bubble_sort(myList)
print(result)
