import numpy as np

def main():
    data = [6,7,8,9,10,11,12]

    Variance = np.var(data)

    Standard_deviation = np.std(data)

    print("Varience :", Variance)
    print("Standard Deviation :", Standard_deviation)

if __name__ == "__main__":
    main()