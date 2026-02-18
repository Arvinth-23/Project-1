from flask import Flask, request, jsonify
from ml_model import ml_predict
from ann_model import ann_predict

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    try:
        study_hours, attendance = map(float, user_input.split(","))

        ml_score = ml_predict(study_hours, attendance)
        ann_score = ann_predict(study_hours, attendance)

        response = f"""
📘 Student Performance Analysis

ML Predicted Score: {ml_score:.2f}
ANN Predicted Score: {ann_score:.2f}

🔍 Insight:
ANN adapts better to complex learning patterns compared to ML.

🎯 Recommendation:
Increase study hours and maintain attendance above 80% for better results.
"""
    except:
        response = (
            "❗ Please enter input as:\n"
            "study_hours, attendance\n\n"
            "Example: 5, 80"
        )

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
