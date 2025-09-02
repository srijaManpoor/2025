class father():
    def fun1(self):
        print("i can do job")
class son(father):
    def fun2(self):
        print("i can play")
ob=son()
ob.fun1()
ob.fun2()
