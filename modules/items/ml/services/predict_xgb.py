import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # folder ml/

MODEL_PATH = os.path.join(BASE_DIR, "model", "xgb_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.pkl")
LABEL_MAP_PATH = os.path.join(BASE_DIR, "model", "label_map.pkl")

# Load model saat aplikasi start
xgb_model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
label_map = joblib.load(LABEL_MAP_PATH)

inv_label_map = {v: k for k, v in label_map.items()}

def predict_text(text: str) -> str:
    X = vectorizer.transform([text])
    pred = xgb_model.predict(X)[0]
    return inv_label_map[pred]
