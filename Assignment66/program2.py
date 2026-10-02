import tensorflow as tf
import matplotlib.pyplot as plt

border = "-"*80
# Input values from -10 to 10
x = tf.linspace(-10.0, 10.0, 100)

# Activation Functions
sigmoid = tf.sigmoid(x)
relu = tf.nn.relu(x)
tanh = tf.nn.tanh(x)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.plot(x, tanh, label="Tanh")

plt.xlabel("Input Values")
plt.ylabel("Activation Output")
plt.title("TensorFlow Activation Functions")
plt.grid(True)
plt.legend()

plt.show()

print(border)

print("Sigmoid: Output range is 0 to 1")
print("ReLU: Negative values become 0, positive values remain unchanged")
print("Tanh: Output range is -1 to 1")

print(border)
