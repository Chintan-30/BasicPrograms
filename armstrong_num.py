# abcd = a^n + b^n + c^n + d^n ,where n = digit of number

n = 8881
# n = int(input("Enter NUM:"))
sum = 0                            #initialy sum is 0       
order = len(str(n))                #lenth of string 
copy_n = n                         #save for if part

while(n>0):                        #
    digit = n%10                   #take single digit from number and store in digit for ex: 1 , 8 , 8, 8, 0
    sum += digit **order           #add the digits qube 1^3 + 8^3 + 8^3 + 8^3
    n = n//10                      # n become 0 after loop termination  :8881//10 = 888 and so on 88, 8, 0

if (sum == copy_n) :               # sum != 8881
    print(f"{copy_n} number is armstrong number")

else:                              
    print(f"{copy_n} is not Armstrong number")
