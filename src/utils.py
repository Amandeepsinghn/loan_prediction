import os 
import pandas as pickle 
import pickle 
import sys
import dill 
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import accuracy_score

def save_object(file_path,obj):
    try:
        dir_name=os.path.dirname(file_path)
        
        os.makedirs(dir_name,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report=[]
        model=models
        model.fit(X_train,y_train)
        
        y_test_pred=model.predict(X_test)
        
        test_model_score=accuracy_score(y_test,y_test_pred)
        
        report.append(test_model_score)
        
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)
    
        
