dataset = tf.data.Dataset.from_tensor_slices((train_x, train_y))
dataset = dataset.batch(32)
dataset = dataset.repeat()
val_dataset = tf.data.Dataset.from_tensor_slices((val_x, val_y)) 
val_dataset = val_dataset.batch(32) 
val_dataset = val_dataset.repeat()
model.fit(dataset, epochs=10, steps_per_epoch=30        
            validation_data=val_dataset, validation_steps=3)













