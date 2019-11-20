# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json

german = pd.read_csv('german_credit.csv')

german_prep = german

target = german_prep['default']
temp = german_prep.drop(['default'], axis = 1)

from sklearn.preprocessing import OneHotEncoder, StandardScaler

german_dummies = temp.select_dtypes(exclude=['int', 'int64', 'float64'])
german_int = temp.select_dtypes(include=['int', 'int64', 'float64'])

german_dummies_2 = pd.get_dummies(german_dummies, drop_first = True)

german_model = pd.concat([german_int, german_dummies_2, target], axis = 1)

x = german_model.iloc[:,0:len(german_model.columns)-1].values
y = german_model.iloc[:,len(german_model.columns)-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0) # test size 20% from train test
SC = StandardScaler()

X_train = SC.fit_transform(X_train)
X_test = SC.fit_transform(X_test)

# Fitting Light GBM to the Training set
import lightgbm as lgb
from lightgbm import LGBMClassifier
lgbm = LGBMClassifier()
lgbm.fit(X_train, y_train)

# Predicting the Test set results
y_pred = lgbm.predict(X_test)

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

lgbm_acc = accuracy_score(y_test, lgbm.predict(X_test))
print(accuracy_score(y_test, lgbm.predict(X_test)))

lgbm_auc = roc_auc_score(y_test, lgbm.predict(X_test))
print(roc_auc_score(y_test, lgbm.predict(X_test)))

# Saving model using pickle
pickle.dump(lgbm, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[1.8]]))