#Convert a 28 x 28 image into a 784 x 1 vector.
x_train = x_train_raw.reshape(60000, 784)
x_test = x_test_raw.reshape(10000, 784)
#Normalize image pixel values. 
x_train = x_train.astype('float32')/255 
x_test = x_test.astype('float32')/255



