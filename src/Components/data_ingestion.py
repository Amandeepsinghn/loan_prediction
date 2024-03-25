import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.Components.data_transformation import DataTransformation
from src.Components.model_trainer import ModelTrainer



@dataclass
class DataingestionConfig():
    train_data_path=os.path.join('artifact','train.csv')
    test_data_path=os.path.join('artifact','test.csv')
    raw_data_path=os.path.join('artifact','data.csv')
    
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()
        
    def initaite_data_ingestion(self):
        logging.info('entering the data ingestion')
        
        try:
            df=pd.read_csv("notebook/data/final_loan.csv")
            
            logging.info('reading the data is completed')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info('train test split has started')
            
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) 
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('ingestion has completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )          
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
            
if __name__=="__main__":
    
    obj=DataIngestion()
    train_data,test_data=obj.initaite_data_ingestion()
    
    obj1=DataTransformation()
    train_arr,test_arr,_=obj1.initiate_data_transformation(train_data,test_data)
    
    
    obj2=ModelTrainer()
    print(obj2.initate_model_training(train_arr,test_arr))
    