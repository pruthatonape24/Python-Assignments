class Demo:
    Value = 0

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def fun(self):
        print("Value of Fun:", self.No1)
        print("Value of Fun:", self.No2)
    
    def gun(self): 
        print("Value of Gun:",self.No1) 
        print("Value of Gun:",self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
print("----"*10)
obj1.gun()
obj2.gun()
    
