from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import pickle
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')


## it says there is a FileNotFoundError with model.pkl file. 

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json    # Get JSON data from the request

    irradiation = data['irradiation']
    module_temperature = data['module_temperature']     # Extract relevant features from JSON data
    
    predicted_ac_output = model.predict([[irradiation, module_temperature]])     # Perform prediction using the loaded model

    return jsonify({'predicted_ac_output': predicted_ac_output[0]})     # Return predicted AC output as JSON response

if __name__ == '__main__':
    model = pickle.load(open(model_path, 'rb')) #importing the ML model using pickle
    app.run(debug=True)

