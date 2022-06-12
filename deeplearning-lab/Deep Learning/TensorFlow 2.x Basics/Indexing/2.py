#Extract the pixel in [1,1] from the first dimension of the first image and the pixel in [2,2] from 
# the first dimension of the second image in tensot_h([4,100,100,3]).
indices = [[0,1,1,0],[1,2,2,0]]
tf.gather_nd(tensor_h,indices=indices)











