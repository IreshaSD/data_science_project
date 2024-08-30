import numpy as np
import pandas as pd
import dill
import sys
import os

from sklearn.metrics import r2_score
from src.exception import CustomException

from sklearn.model_selection import GridSearchCV
# Common object is in utils file

def save_object(file_path,obj): # Help of this function, in the data_transformation we are saving the save_object as a pickle file
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(x_train, y_train,x_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i] 
            para = param[list(models.keys())[i]]

            # gs = GridSearchCV(model,para,cv=3,n_jobs=n_jobs,verbose=verbose,refit=refit)
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train) # gs---> Grid Search CV
            # here cv = cross validation

            model.set_params(** gs.best_params_)
            model.fit(x_train,y_train)

            # model.fit(x_train, y_train) # Train model
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e,sys)
# The reason that this function has been written in utils.py because this is used as a common function throughout the entire project
def load_object(file_path): # responsible for loading the pickle file
    try:
        with open(file_path,"rb") as file_obj: # open the file path in read byte mode and it is loading the pickle file by using the dill
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)



