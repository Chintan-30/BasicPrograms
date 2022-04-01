'''
n! = n * (n-1)!
4! = 4 * 3!
4! = 4 * 3 * 2!
'''
num = int(input("Enter number :\t"))
'''
def fec(num):                    #using function
    if num == 0:
        return 1

    else:
        a = 1
        for i in range(num):
            a = a * (i+1)
    return a        

'''
# a = 1
# for i in range(num):                 #using for loop
#     a = a *(i+1)
'''
i = 1
a = 1
while(i <= num):                        #using while loop
    a = a * (i+1)
    i += 1
'''

# print(a)
# print(f"The fectorial of {num} is ",fec(num)) 


# using recursion

def rec(num):
    if num == 0:
        return 1
    else:
        return num * rec(num-1)

print("Factorial Using Recursive Method", rec(num))
