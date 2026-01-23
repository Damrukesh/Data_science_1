import os
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

from exception import CustomException
from logger import logging

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        import pickle
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            r2_square = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = r2_square
        return report
    except Exception as e:
        raise CustomException(e, sys)    