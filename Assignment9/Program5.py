def DivisibleBy(No):
    if (No % 3 == 0) and (No % 5 == 0):
        return True
    else:
        return False
    
def main():
    Value = int(input("Enter number:"))

    Ret = DivisibleBy(Value)
    print("Divisible by 3 and 5:", Ret)

if __name__ == "__main__":
    main()