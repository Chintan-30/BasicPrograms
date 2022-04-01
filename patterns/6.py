'''
*   
  *
*   *
  *   * 
*   *
  *
* 

'''

'''
n = 4
for i in range (n) :
    print(' ' *(n-i-1) + '* ' *(i+1))'''

n = int(input("enter value: "))
for i in range (n):
    print('* '*(i+1))


for i in range (n-1):
    print('* '*(n-i-1))