# Dependencies
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import urllib.request
import json
import time

READ_API_KEY = '586WDTLPLKR8DM48'
CHANNEL_ID = '1424180'

app = Flask(__name__)
model = pickle.load(open('covid_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    
    predicted_feature = model.predict([ [98, 80, 37] ])
    
    output = predicted_feature[0]

    if predicted_feature == 1:
        output = "You are good. You do not need to go for Covid Test."
    elif predicted_feature == 2:
        output = "You have mild symptoms. You may go for Covid Test."
    elif predicted_feature == 3:
        output = "You have moderate symptoms. You should go for Covid Test."
    elif predicted_feature == 4:
        output = "You have serious symptoms. You must go for Covid Test."

    return render_template('index.html', prediction_text = '{}'.format(output))


if __name__ == "__main__":
    app.run(debug = True)
