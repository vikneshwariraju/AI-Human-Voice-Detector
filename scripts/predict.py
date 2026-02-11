import joblib
import numpy as np
from scripts.features_util import extract_features

MODEL_PATH = "models/voice_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_voice(file_path):

    features = extract_features(file_path)
    features = features.reshape(1, -1)

    prediction = model.predict(features)[0]
    confidence = np.max(model.predict_proba(features)) * 100

    if prediction == 0:
        return f"HUMAN VOICE ({confidence:.2f}% confident)"
    else:
        return f"AI GENERATED VOICE ({confidence:.2f}% confident)"
