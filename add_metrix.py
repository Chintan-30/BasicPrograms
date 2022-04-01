def matrix(m,n):
    o =[]
    for i in range(m):  #row
        row = []
        for j in range(n):  #column
            inp = int(input(f"Enter [{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o    
        
def sum(A,B):
    sum_matrix = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        sum_matrix.append(row)
    return sum_matrix



m = int(input("enter the value of rows:"))
n = int(input("enter the value of columns:"))

print("Emter metrix A:")
A = matrix(m,n)


print("Enter metrix B:")
B = matrix(m,n)
print(A)
print(B)
print('\n')
result = sum(A,B)
print("Sum of given metries is :",result)