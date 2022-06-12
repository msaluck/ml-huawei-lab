#Create a  neural network (DNN) model that consists of four fully connected layers and two RELU activation functions.
model = keras.Sequential([ 
    layers.Dense(784, activation='relu', input_dim = 784),
    layers.Dense(100, activation='relu'),
    layers.Dense(100, activation='relu'),
    layers.Dense(100, activation='relu'),
layers.Dense(num_classes, activation='softmax')])
model.summary() 










