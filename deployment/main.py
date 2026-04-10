import json
import joblib
import numpy as np
import os

def init():
    global model
    # The path Azure uses to store the model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model/model.pkl")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)["data"]
        data = np.array(data)
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        return str(e)
