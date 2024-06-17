from flask import Flask,request,render_template
import numpy as np 
import pandas as pd 


from src.Pipeline.predict_pipeline import CustomData,predict_pipeline

application=Flask(__name__)


app=application


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict',methods=["GET","POST"])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
        rate_of_interest=float(request.form.get('rate_of_interest')),
        
        Interest_rate_spread=float(request.form.get('Interest_rate_spread')),
        Upfront_charges=float(request.form.get('Upfront_charges')),
        property_value=float(request.form.get('property_value')),
        LTV=float(request.form.get('LTV')),
        credit_type=request.form.get('credit_type'),
        dtir1=float(request.form.get('dtir1'))
            
        )
        new_data=data.get_data_dataframe()
        
        pipeline=predict_pipeline()
        pred=pipeline.predict(new_data)
        if pred==[0.]:
            return render_template('form.html',final_result='No')
        else:
            return render_template('form.html',final_result='Yes')
        
    

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
    
    

 

