from config import *
from processing import train, test, X_train, y_train, X_valid, y_valid

model_3 = keras.models.Sequential([
keras.layers.Input(shape=train.shape[-2:]),    
keras.layers.Bidirectional(keras.layers.LSTM(1024, return_sequences=True)),
keras.layers.Bidirectional(keras.layers.LSTM(1024, return_sequences=True)),
keras.layers.BatchNormalization(),
keras.layers.Dropout(0.15),
keras.layers.Bidirectional(keras.layers.LSTM(512, return_sequences=True)),
keras.layers.Bidirectional(keras.layers.LSTM(256, return_sequences=True)),
keras.layers.Bidirectional(keras.layers.LSTM(256, return_sequences=True)),
keras.layers.BatchNormalization(),
keras.layers.Dropout(0.20),
keras.layers.Bidirectional(keras.layers.LSTM(128, return_sequences=True)),
keras.layers.Bidirectional(keras.layers.LSTM(128, return_sequences=True)),
keras.layers.Dropout(0.20),
keras.layers.Dense(128, activation='selu'),
keras.layers.Dense(64, activation='selu'),
keras.layers.Dense(1),
])

optimizer = keras.optimizers.Adam()
model_3.compile(optimizer=optimizer, loss="mae")
model_3.save('model_3.h5')

history_3 = model_3.fit(X_train, y_train, validation_data=(X_valid, y_valid), 
                    epochs=EPOCH, batch_size=BATCH_SIZE, callbacks=[lr, es])

model_3_preds = model_3.predict(test).squeeze().reshape(-1, 1).squeeze()