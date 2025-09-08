class methodoverridding():
    def fun1(self):
        print("i can play")
class child(methodoverridding):
    def fun(self):
        print("i can eat")
        super().fun1()
        #super function is used to access the properties of parent
ob=child()
ob.fun()
