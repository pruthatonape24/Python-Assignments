def NaturalNum(N):
    Sum = 0
    i = 1
    while i <= N:
        Sum = Sum + i
        i = i + 1
    return Sum

def main():
    Value = int(input("Enter a number:"))

    Ret = NaturalNum(Value)
    print("Sum of first N Natural Numbers is:",Ret)

if __name__ == "__main__":
    main()