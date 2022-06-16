import numpy as np
inputs = tf.keras.Input(shape=(3, 1))
lstm = layers.LSTM(1, return_sequences=True)(inputs)
model_lstm_1 = tf.keras.models.Model(inputs=inputs, outputs=lstm)
inputs = tf.keras.Input(shape=(3, 1)) 
lstm = layers.LSTM(1, return_sequences=False)(inputs)
model_lstm_2 = tf.keras.models.Model(inputs=inputs, outputs=lstm)
#Sequences t1, t2, and t3 
data = [[[0.1]
    [0.2],
    [0.3]]]
print(data)
print("output when return_sequencesis set to True",model_lstm_1.predict(data))
print("output when return_sequencesis set to False",model_lstm_2.predict(data))





