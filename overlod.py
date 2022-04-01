#this is method overloding
class A:
    def show(self):
        print("A show")

class B(A):
        def show(self):
           print("B show")
        


b = B()
b.show()