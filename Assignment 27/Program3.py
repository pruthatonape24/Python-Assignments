class Numbers:
    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <=1:
            return False
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
            
        return True
    
    def ChkPerfect(self):
        Sum = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False
    
    def Factors(self):
        print("Factors are:")
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        Sum = 0
        for i in range (1,self.Value+1):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum
    
def main():
    obj1 = Numbers(int(input("Enter Number:")))

    Ret = obj1.ChkPrime()
    if Ret == True:
        print("Number is Prime")
    else:
        print("Number is Not Prime")

    Ret1 = obj1.ChkPerfect()
    if Ret1 == True:
        print("Number is Perfect")
    else: 
        print("Number is Not Perfect") 

    obj1.Factors()

    print("Sum of Factors:", obj1.SumFactors())

if __name__ == "__main__":
    main()      
    
