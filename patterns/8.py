#this is semple fille for practicing



'''n = 3
for i in range (n): #0,1,2
    print(' *'*(n))

'''

'''

 i
 0 *     *  5
 1  *   *   3       space formula =  2n-2i-3
 2   * *    1
 3    *
''' 

'''n = 4
m = 0
for i in range (n-1 ,-1,-1): #3,2,1,0
    print(' ' * (m+1) + ' *' )
    m+=1
'''

n = 4
for i in range(n-1,-1,-1):   # 0,1,2,3
    print('  ' * (i) + ' *' , end ='')
    
    if i!=n-1:
        print('  ' *((2*n) - (2*i) -3) + ' *' , end =' ')
    print()


for i in range(n):   # 0,1,2,3
    print('  ' * (i) + ' *' , end ='')
    
    if i!=n-1:
        print('  ' *((2*n) - (2*i) -3) + ' *' , end =' ')
    print()

