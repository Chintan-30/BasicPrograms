k =0
n = int(input("Enter Number :"))#153

while (n>0):
    i = n%10  #take single digit 3 5 1        
    n = n//10 # update n goes to zero 15 1 0

    k = k*10 + i

print("Reverse Number is :",k)   #351

# k = k*10 + 3
# k = k*10 + 5
# k = k*10 + 1