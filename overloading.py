class Overloading():
    def fun1(self,a=None,b=None,c=None):
        print(a,b,c)
ob=Overloading()
ob.fun1(10,20,30)
ob.fun1(10,20)
ob.fun1(10)
ob.fun1()
