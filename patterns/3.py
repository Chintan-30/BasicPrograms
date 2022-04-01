'''
   * * * 
    * *
     *


'''
    
n = int(input("enter level:"))

for i in range(n , -1, -1):

    for j in range(n):
        print(end=" ")
    n = n + 1
    
    for j in range(i):
        print("*", end=" ")
    print(" ")    
 
 

