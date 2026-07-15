class Circle:
    PI = 3.14

    def __init__(self,R,A,C):
        self.Radius = R
        self.Area = A
        self.Circumference = C

    def Accept(self):
        self.Radius = int(input("Enter Radius:"))
    
    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius
        print("Area of circle is:", self.Area) 
    
    def CalculateCirucumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        print("Circumference of circle is:", self.Circumference)   

    def Display(self):
        self.Accept()
        self.CalculateArea()
        self.CalculateCirucumference()
  
def main():

    obj= Circle(0,0,0)

    obj.Display()

if __name__ == "__main__":
    main()

