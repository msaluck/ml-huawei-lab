#Generate a 100 x 100 x 3 tensor to represent a 100 x 100 three-channel color image. 
expand_sample_1 = tf.random.normal([100,100,3], seed=1)
print("size of the original data:",expand_sample_1.shape)
print("add a dimension before the first dimension (axis= 0):
",tf.expand_dims(expand_sample_1, axis=0).shape)
print("add a dimension before the second dimension (axis= 1):
",tf.expand_dims(expand_sample_1, axis=1).shape) 
print("add a dimension after the last dimension (axis= -1): 
",tf.expand_dims(expand_sample_1, axis=-1).shape)



