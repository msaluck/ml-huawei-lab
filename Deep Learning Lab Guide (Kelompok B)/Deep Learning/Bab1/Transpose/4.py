#During the operation, if two arrays have different shapes, TensorFlow automatically triggers the broadcast mechanism as NumPy does.
a = tf.constant([[3, 5], [4, 8]])
b = tf.constant([[1, 6], [2, 9]])
print(tf.add(a, b))









