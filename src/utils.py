import numpy as np
import pandas as pd
import dill
import sys
import os

from src.exception import CustomException
# Common object is in utils file

def save_object(file_path,obj): # Help of this function, in the data_transformation we are saving the save_object as a pickle file
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

