import pandas as pd
import logging
import numpy as np
import pickle
from joblib import dump, load
from sklearn.model_selection import train_test_split


from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

def run_training():
    #trains model
    dataset = pd.read_csv('BU_MBA_salaries.csv')
    X = pd.DataFrame(dataset.iloc[:,:-1])
    y = pd.DataFrame(dataset.iloc[:,-1])
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    regressor = RandomForestRegressor(n_estimators=20, random_state=0)
    model = regressor.fit(X_train, y_train.values.ravel())
    y_pred = model.predict(X_test)

    print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_pred))
    print('Mean Squared Error:',metrics.mean_squared_error(y_test,y_pred))
    print('Root Mean Absolute Error:',np.sqrt(metrics.mean_absolute_error(y_test,y_pred)))

    #persist trained model
    dump(regressor, 'randomForest.joblib')

def RFpredict(array):
    regressor = load('randomForest.joblib')

    return regressor.predict(pd.DataFrame([array]))