# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:43:19 2019

@author: INTEL
"""

import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


# Load the model
model = pickle.load(open('houseprice.pkl','rb'))

app = Flask(__name__)

@app.route('/api',methods=['POST'])
def predict_model():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = data
    prediction = np.array(prediction)
    # Take the first value of prediction
    y_ash = model.predict(prediction)
    output = [y_ash[0]]
    return jsonify(results=output)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
