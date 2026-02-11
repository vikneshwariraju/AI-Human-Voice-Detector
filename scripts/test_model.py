import numpy as np
import joblib
from sklearn.metrics import accuracy_score, classification_report

X_test = np.load("data/processed/X_test.npy")
y_test = np.load("data/processed/y_test.npy")

model = joblib.load("models/voice_model.pkl")

predictions = model.predict(X_test)

print("Test Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

print("X_test shape:", X_test.shape)

