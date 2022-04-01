''' 
  n is 4
i 

0    *     
1   * *   1 space between 2 star        
2  *   *  3         
3 *     * 5           formula = 2i -1 
2  *   *  3 
1   * *   1
0    *
 '''

n = int(input("enter level: "))        #4

for i in range (n): #0,1,2,3
    print('  '* (n-i-1) + '* ',end = '')    
  
    if i>=1:
        print('  ' * (2*i-1) + '*' ,end ='')
    print( )

for i in range(n):   # 0,1,2,3
    print('  ' * (i) + ' *' , end ='')
    
    if i!=n-1:
        print('  ' *((2*n) - (2*i) -3) + ' *' , end =' ')
    print()
