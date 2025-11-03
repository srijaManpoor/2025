class grandfather():
    def __init__(self):
        self._a=10
        self._b=20
        def _fun3(self):
            print("i have farmhouse")
class father(grandfather):
    def fun1(self):
        print("i have 10 acres of land")
class son(father):
    def fun2(self):
        print("i have 10 crores amount")
ob=son()
ob.fun2() 
