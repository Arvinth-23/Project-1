import pandas as pd
from sklearn.linear_model import LinearRegression

def ml_predict(study_hours, attendance):
    data = pd.read_csv("student_data.csv")

    X = data[['study_hours', 'attendance']]
    y = data['score']

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[study_hours, attendance]])
    return prediction[0]
