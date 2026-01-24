import os
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        import pickle
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    return file_path

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        fitted_models = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=params[list(models.keys())[i]]
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_test_pred = gs.predict(X_test)
            r2_square = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = r2_square
            # Store the fitted model
            fitted_models[list(models.keys())[i]] = model
        return report, fitted_models
    except Exception as e:
        raise CustomException(e, sys)    
def load_object(file_path):
    try:
        import pickle
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)