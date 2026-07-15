class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        amount = int(input("Enter amount to deposit:"))
        self.Amount = self.Amount + amount
    
    def Withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.Amount:
            self.Amount = self.Amount - amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI)/100
        return Interest
    
def main():
    Name = input("Enter Account Holder Name:")
    Amount = int(input("Enter Amount:"))

    obj1 = BankAccount(Name,Amount)

    print("\nAccount Details:")
    obj1.Display()
    obj1.Deposit()
    obj1.Display()
    obj1.Withdraw()
    obj1.Display()
    print("Interest is:", obj1.CalculateInterest())

if __name__ == "__main__":
    main()