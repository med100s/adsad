arr = []
for i in range(489421,489440):
    for d in range(1, 489440):
        if i % d == 0:
            arr.append(d)
    if len(arr) == 4:
        print(i, arr)
    arr = []
    
    
  

#489421 [1, 19, 25759, 489421]                                                                                                                                                      
#489422 [1, 2, 244711, 489422]                                                                                                                                                      
#489437 [1, 13, 37649, 489437]                                                                                                                                                      
                                 
