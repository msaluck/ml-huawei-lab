#Use the timeitmodule to measure the execution time of a small code segment.
import timeit
#Create a convolutional layer.
CNN_cell = tf.keras.layers.Conv2D(filters=100,kernel_size=2,strides=(1,1)) 
#Use @tf.functionto convert the operation into a graph.
@tf.function
def CNN_fn(image):
    return CNN_cell(image)
image = tf.zeros([100, 200, 200, 3])
#Compare the execution time of the two modes.
CNN_cell(image)
CNN_fn(image) 
#Call timeit.timeitto measure the time required for executing the code 10 times.
print("time required for performing the computation of one convolutional neural network (CNN)
layer in eager execution mode:", timeit.timeit(lambda: CNN_cell(image), number=10))
print("time required for performing the computation of one CNN layer in graph mode:", 
timeit.timeit(lambda: CNN_fn(image), number=10))    