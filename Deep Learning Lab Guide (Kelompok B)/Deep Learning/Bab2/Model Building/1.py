#Create a fully connected layer that contains 32 neurons. Set the activation function to sigmoid.
#The activationparameter can be set to a function name string, for example, sigmoidor a function object, for example, tf.sigmoid.
layers.Dense(32, activation='sigmoid')
layers.Dense(32, activation=tf.sigmoid)
#Set kernel_initializer. 
layers.Dense(32, kernel_initializer=tf.keras.initializers.he_normal)
#Set kernel_regularizerto L2 regularization. 
layers.Dense(32, kernel_regularizer=tf.keras.regularizers.l2(0.01))







