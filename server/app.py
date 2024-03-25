from flask import Flask, request, jsonify
import sklearn
import numpy as np
import pickle
import os

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "<h1>API is working...</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json    # Get JSON data from the request

    irradiation = data['irradiation']
    module_temperature = data['module_temperature']     # Extract relevant features from JSON data
    
    predicted_ac_output = model.predict([[irradiation, module_temperature]])     # Perform prediction using the loaded model

    return jsonify({'predicted_ac_output': predicted_ac_output[0]})     # Return predicted AC output as JSON response

if __name__ == '__main__':
    model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
    model = pickle.load(open(model_path, 'rb'))
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))