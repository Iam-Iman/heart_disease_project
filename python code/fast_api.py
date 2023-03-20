# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:23:43 2023

@author: Iman Ngwepe
"""
# Public Host  
import json
import requests

url = 'http://3b70-102-249-2-81.ngrok.io/heart_disease_prediction'


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