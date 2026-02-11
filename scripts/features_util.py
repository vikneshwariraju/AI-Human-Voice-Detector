import numpy as np
import librosa

import numpy as np
import librosa

def extract_features(file_path):

    audio, sr = librosa.load(file_path, sr=22050,mono=True)

    mfcc = np.mean(
        librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13).T,
        axis=0
    )

    zcr = np.mean(librosa.feature.zero_crossing_rate(audio))
    spec_centroid = np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr))
    spec_rolloff = np.mean(librosa.feature.spectral_rolloff(y=audio, sr=sr))

    features = np.hstack([mfcc, zcr, spec_centroid, spec_rolloff])

    return features.reshape(1, -1)

