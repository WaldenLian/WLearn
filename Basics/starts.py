import numpy as np
import tensorflow as tf 

# Trainable parameters
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# Input and Label Input 
x = tf.placeholder(tf.float32)
linear_model = W * x + b 
y = tf.placeholder(tf.float32)

# Loss function
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Training data 
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
# Training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # Reset values to wrong
for i in range(1000):
    sess.run(train, feed_dict={x: x_train, y: y_train})

# Evaluate the training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss))

