x = tf.ones((2, 2), dtype=tf.dtypes.float32)
y = tf.constant([[1, 2],
                        [3, 4]], dtype=tf.dtypes.float32)
z = tf.matmul(x, y)
print(z)


