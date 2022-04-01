'''
*
* *
* * *
* * * *
* * *
* *
*
'''
import time
n = int(input("enter value:"))

for i in range (n):
    print('* ' * (i+1))
    time.sleep(0.5)
for i in range(n-1):
    print('* ' * (n-i-1))
    time.sleep(0.5)