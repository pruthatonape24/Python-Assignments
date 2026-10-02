import tensorflow as tf

border = "-"*80

inputs = tf.constant([2.0,3.0])

weights = tf.constant([0.4,0.6])

bias = tf.constant(0.5)

weights = tf.reduce_sum(inputs * weights) + bias
output = tf.sigmoid(weights)


print(border)
print("Weighted sum:",weights)
print("Sigmoid:",output)
print(border)