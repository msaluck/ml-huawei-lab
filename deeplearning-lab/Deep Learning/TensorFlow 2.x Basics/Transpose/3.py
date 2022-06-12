#During the operation, if two arrays have different shapes, TensorFlow automatically triggers the broadcast mechanism as NumPy does.
a = tf.constant([[ 0, 0, 0],
                [10,10,10],
                [20,20,20],
                [30,30,30]])
b = tf.constant([1,2,3])
print(a + b)
