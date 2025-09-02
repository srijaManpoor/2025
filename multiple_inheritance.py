class father():
    def fun1(self):
        print("i can do job")
class mother():
    def fun2(self):
        print("i can cook")
class daughter(father,mother):
    def fun3(self):
        print("i can study")
ob=daughter()
ob.fun3()
ob.fun2()
ob.fun1()
