#Set hyperparameters. 
Epochs = 10
#Define a function for dynamically setting the learning rate.
def lr_Scheduler(epoch):
    if epoch > 0.9 * Epochs
        lr = 0.0001
    elif epoch > 0.5 * Epochs:
        lr = 0.001
    elif epoch > 0.25 * Epochs: 
        lr = 0.01
    else:
        lr = 0.1
    print(lr)
    return lr
callbacks = [ 
    #Early stopping:
    tf.keras.callbacks.EarlyStopping(
        #Metric for determining whether the model performance has no further improvement monitor='val_loss',improvement
        min_delta=1e-2,
        #Number of epochs in which the model performance has no further improvement patience=2),
    #Periodically save models.
    tf.keras.callbacks.ModelCheckpoint( 
        #Model path
        filepath='testmodel_{epoch}.h5',
        #Whether to save the optimal model.
        save_best_only=True, 
        #Monitored metric 
        monitor='val_loss'), 
    #Dynamically change the learning rate.
    tf.keras.callbacks.LearningRateScheduler(lr_Scheduler),
    #Use TensorBoard.
    tf.keras.callbacks.TensorBoard(log_dir='./logs')
]
model.fit(train_x, train_y, batch_size=16, epochs=Epochs, 
    callbacks=callbacks, validation_data=(val_x, val_y))




