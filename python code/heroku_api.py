# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 07:20:26 2023

@author: Iman Ngwepe
"""

# Heroku   
import json
import requests

# Local host 
#url = 'http://127.0.0.1:8000/heart_disease_prediction'

# Heroku
url = 'https://heart-disease-model-heroku.herokuapp.com/heart_disease_prediction'


input_data_for_model = {
    
    'age' : 63,
    'sex' : 1,
    'cp' : 3,
    'trestbps' : 145,  
    'chol' : 233,
    'fbs' : 1,
    'restecg' : 0,
    'thalach' : 150,
    'exang' : 0,
    'oldpeak' : 2.3,
    'slope' :  0,
    'ca' : 0,
    'thal' : 1
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)