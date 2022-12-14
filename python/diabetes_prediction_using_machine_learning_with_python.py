# -*- coding: utf-8 -*-
"""Diabetes Prediction using Machine Learning with Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g1GoJEEd-kdsQ0v03JmNgXP3YIQcCQpe

1. Import the lib
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler     # --> to stander the daata for svm
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""2. Load datasets"""

df = pd.read_csv("diabetes.csv")

"""3. Analysis"""

df.head(10)

df.info()

df.shape

df.isnull().sum

df.describe()

df['Outcome'].value_counts()

"""0 --> Non-Diabetic
1 --> Diabetic
"""

df.groupby('Outcome').mean()

df.groupby('Outcome').median()

"""4. Defining X and Y"""

# separating x and y

x = df.drop(columns='Outcome', axis = 1)  # axis = 1 means we are droping column or axis = 0 means we are dropin row
y = df['Outcome']

print(x)

print(y)

"""5. Data Standardization"""

scaler = StandardScaler()

scaler .fit(x)

standerdized_data = scaler.transform(x)

print(standerdized_data)   # --> this is use for converting the data into same range

x = standerdized_data
y = df['Outcome']

"""5. tarin test split"""

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, stratify=y)

# stratify=y means if we dont use this it may cause like all the 0's gose to test and 1's goes to train and it may case to model
# with the help of this it classify in same ratio

print(x.shape, x_train.shape, x_test.shape)

print(y.shape, y_train.shape, y_test.shape)

"""6. Tarining the model """

classifir = svm.SVC(kernel='linear')

#training the svm classifier

classifir.fit(x_train,y_train)

"""7. Model Evaluation

Accuracy Score For Train data
"""

x_train_prediction = classifir.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy score of training data: ',training_data_accuracy)

"""Accuracy Score For Test data"""

x_test_prediction = classifir.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy score of test data: ',test_data_accuracy)

"""Making a Predictive System"""

input_data=[6,148,72,35,0,33.6,0.627,50]

#changing the input data into the numpy array
input_data_array = np.asanyarray(input_data)
#reshaping the array into 2d in one row
input_data_reshape = input_data_array.reshape(1,-1)
#standerd the input
std_data = scaler.transform(input_data_reshape)

prediction = classifir.predict(std_data)
#print(prediction)

if prediction[0]==0:
  print('the person is not diabetic')
else:
  print('the person is diabetic')

