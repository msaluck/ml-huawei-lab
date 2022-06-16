#Extract the first, second, and fourth images from tensor_h([4,100,100,3]). 
indices = [0,1,3]
tf.gather(tensor_h,axis=0,indices=indices,batch_dims=1)













