num = {2,3,3,34,4,5,4,6}                #set

even = list(filter(lambda n : n%2 == 0 ,num))
print("filterd evens:",even)                                                  #filter is used for filter the objects


doubles = list(map(lambda n : n*2 , num))
print("map",doubles)                                             # applying an operation to each item and collect the result.

'''
The reduce is in the functools in Python 3.0. 
It is more complex. It accepts an iterator to process, 
but it's not an iterator itself. It returns a single result:
''' 
from functools import reduce

sum = reduce(lambda n,m: n+m , num )
print("reduce",sum)

