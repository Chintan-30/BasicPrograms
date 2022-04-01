#fibonacci seris  
# 0 1 1 2 3 5 8 13

x = 0
y = 1

_num = int(input("how many numbers want to print:\t"))
print(x)
print(y)
while(1):
    a = x + y
    x = y 
    y = a
    
    print(a)
    if (a>_num):
        break
    


'''
a = x + y 
b = y + a
c = a + b

print(x , y , a , b , c )

'''