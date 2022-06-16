#LSTM
tf.keras.layers.LSTM(16, return_sequences=True)
#LSTMCell
x = tf.keras.Input((None, 3))
y = layers.RNN(layers.LSTMCell(16))(x)
model_lstm_3= tf.keras.Model(x, y)
