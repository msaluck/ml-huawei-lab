Optimizer = optimizers.Adam(0.001)
model.compile(loss=keras.losses.categorical_crossentropy, 
                optimizer=Optimizer,
                metrics=['accuracy']) 
# Training the NN Model
#Fit the training data to the model by using the fit method.
model.fit(x_train, y_train, 
            batch_size=128,
            epochs=10,
            verbose=1) 

