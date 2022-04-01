'''this is file reading program 
the file is me.txt 
print all the line of this file'''



f = open("me.txt" , "r")
# contant = f.read()
# print(contant)
print(f.readline())

# for line in f:
#     print(line)


f.close()