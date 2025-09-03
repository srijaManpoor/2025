class father(): 
    def fun1(self):
        print("father have 300 crores")
class son1(father):
    def fun2(self):
        print("i have 100cr")
class son2(father):
    def fun3(self):
        print("i have 100cr")
class son3(father):
    def fun4(self):
        print("i have 100cr")
ob=son1()
ob.fun1()
ob.fun2()
ob=son2()
ob.fun1()
ob.fun3()
ob=son3()
ob.fun1()
ob.fun4()
