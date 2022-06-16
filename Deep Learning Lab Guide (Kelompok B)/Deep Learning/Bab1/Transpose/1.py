#Generate an $ x 100 x 200 x 3 tensor to represent four 100 x 200 three-channel color images. 
trans_sample_2 = tf.random.normal([4,100,200,3])
print("size of the original data:",trans_sample_2.shape)
#Exchange the length and width for the four images: The original permvalue is [0,1,2,3], and 
the new permvalue is [0,2,1,3]. 
transposed_sample_2 = tf.transpose(trans_sample_2,[0,2,1,3])
print("size of transposed data:",transposed_sample_2.shape)



