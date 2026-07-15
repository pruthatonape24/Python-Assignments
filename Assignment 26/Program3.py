class Arithmatic: 
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Accept(self):
        self.Value1 = self.No1
        self.Value2 = self.No2

    def Addition(self):
        Ans = self.Value1 + self.Value2
        return Ans

    def Substraction(self):
        Ans = self.Value1 - self.Value2
        return Ans
    
    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        return Ans
    
    def Division(self):
        Ans = self.Value1 / self.Value2
        return Ans   

def main():

    Value1 = int(input("Enter First number:"))

    Value2 = int(input("Enter Second number:"))

    Aobj = Arithmatic(Value1,Value2)

    Aobj.Accept()

    print("Addition is :", Aobj.Addition())

    print("Subtraction is:", Aobj.Substraction())

    print("Multiplication is:", Aobj.Multiplication())

    print("Division is:", Aobj.Division())

if __name__ == "__main__":
    main()
