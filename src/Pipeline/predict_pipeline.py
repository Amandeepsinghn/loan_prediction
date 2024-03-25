import sys
import os 
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd 


class predict_pipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            
            preprocessor_path=os.path.join('artifact','proprocessor.pkl')
            model_path=os.path.join('artifact','model.pkl')
            
            preprocessor=load_object(file_path=preprocessor_path)
            model=load_object(file_path=model_path)
            
            data_scaled=preprocessor.transform(features)
            
            pred=model.predict(data_scaled)
            
            
        except Exception as e:
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,rate_of_interest:float,Interest_rate_spread:float,Upfront_charges:float,property_value:float,LTV:float,credit_type:str,dtir1:float):
        self.rate_of_interest=rate_of_interest
        self.Interest_rate_spread=Interest_rate_spread
        self.Upfront_charges=Upfront_charges
        self.property_value=property_value
        self.LTV=LTV
        self.credit_type=credit_type
        self.dtir1=dtir1
        
    def get_data_dataframe(self):
        try:
            custom_data_input={
                'rate_of_interest':[self.rate_of_interest],
                'Interest_rate_spread':[self.Interest_rate_spread],
                'Upfront_charges':[self.Upfront_charges],
                'property_value':[self.property_value],
                'LTV':[self.LTV],
                'credit_type':[self.credit_type],
                'dtir1':[self.dtir1]
            }
            df=pd.DataFrame(custom_data_input)
            logging.info('dataframe has been made')
            return df
        
        except Exception as e:
            raise(CustomException(e,sys))
        
