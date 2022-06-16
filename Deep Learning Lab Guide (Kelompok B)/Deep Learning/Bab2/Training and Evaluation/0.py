model = tf.keras.Sequential()
model.add(layers.Dense(10, activation='softmax'))
#Determine the optimizer (optimizer), loss function (loss), and model evaluation method
(metrics).
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
            loss=tf.keras.losses.categorical_crossentropy,
            metrics=[tf.keras.metrics.categorical_accuracy])










