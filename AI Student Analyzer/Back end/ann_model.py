import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def ann_predict(study_hours, attendance):
    data = pd.read_csv("student_data.csv")

    X = data[['study_hours', 'attendance']].values
    y = data['score'].values

    model = Sequential()
    model.add(Dense(10, activation='relu', input_shape=(2,)))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=60, verbose=0)

    prediction = model.predict(np.array([[study_hours, attendance]]))
    return prediction[0][0]
