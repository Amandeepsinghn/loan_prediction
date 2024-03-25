import os 
from sklearn.tree import DecisionTreeClassifier
from dataclasses import dataclass 
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models
from sklearn.metrics import accuracy_score


@dataclass
class ModelTraninerConfig:
    trained_model_path=os.path.join('artifact','model.pkl')
    

class ModelTrainer:
    def __init__(self):
        self.model_training_config=ModelTraninerConfig()
        
        
    def initate_model_training(self,train_array,test_array):
        try:
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            model1=DecisionTreeClassifier()
            
            model_report=evaluate_models(X_train,y_train,X_test,y_test,models=model1)
            
            best_model=model1
            
            save_object(file_path=self.model_training_config.trained_model_path,
                        obj=best_model)
            
            return model_report
        
        
        except Exception as e:
            raise CustomException(e,sys)
            
            
            