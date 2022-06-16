@tf.function
def simple_nn_layer(w,x,b): 
    print(b)
    return tf.nn.relu(tf.matmul(w, x)+b)
w = tf.random.uniform((3, 3)) 
x = tf.random.uniform((3, 3))     
b = tf.constant(0.5, dtype='float32')    
simple_nn_layer(w,x,b)    
    