'''
      *
    *   *
   *  *  *
 *  *   *  *

'''


n = int(input("enter level:"))

for i in range(n):
    
    for j in range(n):
        print(end=" ")
    n = n - 1  

    for j in range(i + 1):
        print("*", end=" ")
    print(" ")



'''n = int(input("enter level:"))
for i in range(n):
    print(' ' *(n-i-1) + '* ' *(i+1))

for i in range(n-1):                                #for piramid
    print(' ' *(i+1) + '* ' *(n-i-1))'''