Optimizer = optimizers.Adam(0.001)
model.compile(loss=keras.losses.categorical_crossentropy, 
                optimizer=Optimizer,
                metrics=['accuracy']) 







