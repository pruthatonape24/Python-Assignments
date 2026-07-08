def FactorSum(No):
    Sum = 0
    for i in range(1, No+1):
        if No % i == 0:
            Sum = Sum + i
    return Sum
    
def main():
    value = int(input("Enter a number:"))
    Ret = FactorSum(value)
    print("Sum of its factor is :", Ret)

if __name__ == "__main__":
    main()