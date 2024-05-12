from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import librosa
import librosa.feature
import numpy as np


def extract_feature(file_name, mfcc=True, chroma=True, mel=True):
    X, sample_rate = librosa.load(os.path.join(file_name), res_type='kaiser_fast')
    if chroma:
        stft = np.abs(librosa.stft(X))
    result = np.array([])
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result = np.hstack((result, mfccs))
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        result = np.hstack((result, chroma))
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mel))
    return result



# predict.py

def predict_emotion(audio_file_path):
    mfcc_features = extract_feature(audio_file_path, mfcc=True, chroma=True, mel=True)

    trained_model = joblib.load('D:\Workspace\ED\Emotion_Detection_ML\model_filename.pkl')  # Replace with the path to your trained model file

    predicted_label = trained_model.predict(mfcc_features.reshape(1, -1))

    return predicted_label
