from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(500):        
            print("hay")
            sleep(1)



class Hi(Thread):
    def run(self):
        for i in range(500):
            print("chintan")
            sleep(1)


t1 = Hello()      #creation of thread
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()



'''
# telusko
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()
'''