#protected

class A:
    def __init__(self,a,b):
        self._a=a
        self._b=b

class B(A):
     def showA(self):
        a = A(20,30)#it cannot inherit this values
        print(a._a)


obj = B(10,20)    
obj.showA()
print(obj._a)
print(obj._b)

# print(obj.a) # not accessible 
# print(obj.b) # not accessible 
