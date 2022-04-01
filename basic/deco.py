'''
decorator is used to add extra feature in exesting function

too change behavier of function

'''
# supose we wants to division of two numbers but always denominator number is always smaller than numerator
#   3/4 where 3 is numerator and 4 is denomirator   


def div(a , b):
    return(a/b)

def samrt_div(func):                                  ############
   
    def inner(a,b):
        if a < b:
            a,b = b,a                                   #this is is decorator
            return func(a,b)
    return inner
                                                       ##############


print(div(4,2))

div = samrt_div(div)
print(div(2,4))