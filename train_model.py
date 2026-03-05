import pandas as pd
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

print("Creating dataset internally...")

# Create dataset manually (NO CSV NEEDED)
data = {
    "label": [
        "ham","spam","ham","spam","ham","spam","ham","spam","ham","spam",
        "ham","spam","ham","spam","ham","spam","ham","spam","ham","spam"
    ],
    "text": [
        "Hey are we meeting tomorrow?",
        "Congratulations! You have won a free prize click now",
        "Please send me the report by evening",
        "Urgent your account has been compromised verify immediately",
        "Can we reschedule the meeting?",
        "You have been selected for a cash reward",
        "Let's grab lunch today",
        "Win money now limited time offer",
        "Thank you for your help",
        "Claim your free vacation now",
        "I will call you later",
        "Your password expires today click here to reset",
        "Are you coming to the party?",
        "Crypto investment opportunity guaranteed profit",
        "Meeting postponed to next week",
        "Exclusive deal just for you act fast",
        "Please review the attached document",
        "Free entry in weekly competition reply now",
        "Happy birthday have a great day",
        "You won a lottery send bank details immediately"
    ]
}

df = pd.DataFrame(data)

# Convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

df['text'] = df['text'].apply(clean_text)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Accuracy
y_pred = model.predict(X_test_vec)
print("Model Accuracy:", round(accuracy_score(y_test, y_pred)*100, 2), "%")

# Save files
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model saved successfully!")