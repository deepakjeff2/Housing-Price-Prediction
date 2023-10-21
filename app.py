import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

#loading the pickle files
scaler = pickle.load(open('scaler.pkl','rb'))
regression = pickle.load(open('regmodel.pkl','rb'))

#creating app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = regression.predict(new_data)
    print(output)
    return jsonify(output[0])