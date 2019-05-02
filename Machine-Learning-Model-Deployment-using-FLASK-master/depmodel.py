# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import pickle
import requests
import json
# Importing the dataset
data = pd.read_csv(r'C:\Users\INTEL\Desktop\BeePec\housepricedata.csv')
print(data.head())
print(data.isnull().sum())
X = data.drop('AboveMedianPrice',axis=1).values
scaled = MinMaxScaler()
X = scaled.fit_transform(X)
y = data['AboveMedianPrice'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
# Fitting Simple Linear Regression to the Training set
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test)
# Saving model to disk
pickle.dump(classifier, open('houseprice.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('houseprice.pkl','rb'))
print(model.predict([[8450,7,5	,856,	2,	1,	3,	8,	0,	548]]))


#import requests
url = 'http://localhost:5000/api'
data = json.dumps({'LotArea':8450,'OverallQual':7,'OverallCond':5,
                   'TotalBsmtSF':856,
                   'FullBath':2,
                   'HalfBath':1,
                   'BedroomAbvGr':3,
                   'TotRmsAbvGrd':8,
                   'Fireplaces':0,
                   'GarageArea':548})
r = requests.post(url,data=data)
r.raise_for_status()
print(r.json())
