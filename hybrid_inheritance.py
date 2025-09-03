class grandparents():
    def fun1(self):
        print("lets have a party")
class father(grandparents):
    def fun2(self):
        print("i will arrange everything")
class mother(grandparents):
    def fun3(self):
        print("i will prepare food for us")
class children(father,mother):
    def fun4(self):
        print("lets have fun")
ob=children()
ob.fun1()
ob.fun2()
ob.fun3()
ob.fun4()

    
