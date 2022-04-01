#0 1 2 3 5 8 13 21

x = 0
y = 1

num = int(input("range :"))  

print(x)
print(y)

for i in range(0,num-2):
  a = x + y
  x = y
  y = a 
  print(a)

'''while(True):
    a = x + y
    x,y = y,a 
    print(a )
    if a>num:
    	break    
        
    '''
