import TensorFlow as tf
thre_1 = tf.random.uniform([], 0, 1) 
x = tf.reshape(tf.range(0, 4), [2, 2])
print(thre_1) 
if thre_1.numpy() > 0.5:
    y = tf.matmul(x, x)
else:
    y = tf.add(x, x)