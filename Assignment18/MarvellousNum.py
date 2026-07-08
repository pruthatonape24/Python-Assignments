def ChkPrime(No):
    if No <=1:
        return False
    i = 2
    if No == i:
        return True
    
    if No % i == 0:
        return False
    else:
        return True
    
def AddPrime(Data):
    Sum = 0

    for i in Data:
        if ChkPrime(i):
            Sum = Sum + i

    return Sum