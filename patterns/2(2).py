'''
      1
    2   3
   4  5  6
 7  8   9  10

'''



n = int(input("enter level:"))
c =0
for i in range(n):
    
    for j in range(n):
        print(end=" ")
    n = n - 1  

    for j in range(i + 1):
        
            print(c+1, end=" ")
            c+=1
    print(" ")


