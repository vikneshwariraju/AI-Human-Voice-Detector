import os
import numpy as np
from features_util import extract_features

HUMAN_PATH = "data/raw/Test/Human"
AI_PATH = "data/raw/Test/ai-generated"

OUTPUT_X = "data/processed/X_test.npy"
OUTPUT_Y = "data/processed/y_test.npy"

X = []
Y = []

# Human = 0
for file in os.listdir(HUMAN_PATH):
    if file.endswith(".wav"):
        path = os.path.join(HUMAN_PATH, file)
        X.append(extract_features(path))
        Y.append(0)

# AI = 1
for file in os.listdir(AI_PATH):
    if file.endswith(".wav"):
        path = os.path.join(AI_PATH, file)
        X.append(extract_features(path))
        Y.append(1)

X = np.array(X)
Y = np.array(Y)

os.makedirs("data/processed", exist_ok=True)

np.save(OUTPUT_X, X)
np.save(OUTPUT_Y, Y)

print("✅ Features Extracted Successfully")
print("X shape:", X.shape)
print("Y shape:", Y.shape)
