from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the fixed model and feature names
with open('parkinsson_fixed.pkl', 'rb') as f:
    model = pickle.load(f)
    print(f"Model type: {type(model)}")

with open('feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)
    print(f"Feature names: {feature_names}")

@app.route('/')
def index():
    return render_template('index.html', features=feature_names, prediction=None, probability=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get features from form
        features = [float(request.form[feature]) for feature in feature_names]
        input_array = np.array([features])
        
        # Make prediction
        prediction = model.predict(input_array)[0]
        probabilities = model.predict_proba(input_array)[0]
        
        # Determine result and probability
        if prediction == 1:
            result = "Parkinson's Disease Detected 🧠"
            probability = f"{probabilities[1]*100:.1f}%"
        else:
            result = "No Parkinson's Disease ✅"
            probability = f"{probabilities[0]*100:.1f}%"
        
        print(f"Prediction: {prediction}, Probabilities: {probabilities}")
        
        return render_template('index.html', 
                             features=feature_names, 
                             prediction=result, 
                             probability=probability)
    except Exception as e:
        return render_template('index.html', 
                             features=feature_names, 
                             prediction=f"⚠️ Error: {e}", 
                             probability=None)

if __name__ == '__main__':
    app.run(debug=True) 