import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

X = np.load("data/processed/X_train.npy")
Y = np.load("data/processed/y_train.npy")

print("X Shape:", X.shape)
print("Y Shape:", Y.shape)

X_train, X_val, y_train, y_val = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_val)

print("Accuracy:", accuracy_score(y_val, pred))
print(classification_report(y_val, pred))

joblib.dump(model, "models/voice_model.pkl")
print("✅ Model saved successfully")
