'''n = int(input("Enter then number"))

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

print("Factorial Using Iterative Method", factorial_iterative(n))


def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print("Factorial Using Recursive Method", factorial_recursive(n))

'''

# 0 1 1 2 3 5 8 13 fibonacci
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
        print(n)
