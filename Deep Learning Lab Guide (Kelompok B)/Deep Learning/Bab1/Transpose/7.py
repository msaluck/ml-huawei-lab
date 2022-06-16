reduce_sample_1 = tf.constant([1,2,3,4,5,6],shape=[2,3]) 
print("original data",reduce_sample_1.numpy())
print("calculate the sum of all elements in the tensor (axis= None):
",tf.reduce_sum(reduce_sample_1,axis=None).numpy()) 
print("calculate the sum of elements in each column by column (axis= 0): 
",tf.reduce_sum(reduce_sample_1,axis=0).numpy()) 
print("calculate the sum of elements in each column by row (axis= 1):
",tf.reduce_sum(reduce_sample_1,axis=1).numpy())









