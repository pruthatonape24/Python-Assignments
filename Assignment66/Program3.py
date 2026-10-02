import numpy as np

# Actual values
Y = [1, 0, 1, 1, 0]

# Predicted values
yp = [0.9, 0.2, 0.8, 0.7, 0.1]

n = len(Y)

print("Actual values   :", Y)
print("Predicted values:", yp)
print("Length          :", n)

# --------------------------------------
# Calculate Squared Error

se = [(Y[i] - yp[i])**2 for i in range(n)]

for s in se:
    print(f"Squared Error: {s:.2f}")

# --------------------------------------
# Calculate MSE

Mse = sum((Y[i] - yp[i])**2 for i in range(n)) / n

print("MSE:", Mse)