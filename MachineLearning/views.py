from django.shortcuts import render
import json
import joblib
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
import pandas as pd
import numpy as np
# Create your views here.
def dataPreprocessing(data):
        # Create a DataFrame from the dictionary
    column=[ 'Gender', 'Married', 'Education', 'Self_Employed', 'Credit_History','Property_Area' ]
    df = pd.DataFrame(data, index=['0'])
    # Create a DataFrame from the dictionary
    feature_values={
                
                'Gender':['Male', 'Female', 'None'],
                'Married':['Yes', 'No', 'None'],
                'Education':['Graduate', 'No_Graduate', 'None'],
                'Self_Employed':['Yes', 'No', 'None'],
                'Credit_History':['Yes', 'No', 'None'],
                'Property_Area':['Urban', 'Rular', 'Semiurban']
                
               }
    # Provide 5 prefixes (one for each column)
    df=pd.get_dummies(df,column)
    column_names_list_df1=df.columns.tolist()
    df2=pd.DataFrame(feature_values)
    df2=pd.get_dummies(df2,column)
    # Get column names
    column_names_list = df2.columns.tolist()
    for col in column_names_list:
        if col not in column_names_list_df1:
            df[col] =0 
    pattern_char = 'None'  # Character to match in column names

# Filter columns containing the character using list comprehension
    columns_to_drop = [col for col in df.columns if pattern_char in col]
    # Drop the filtered columns
    df=df.drop(columns_to_drop, axis=1)
    #print(df)
    return df

def predictions(df):
        model=joblib.load('MachineLearning\loan_model.pkl')
        scaler=joblib.load('MachineLearning\scaler.pkl')
        # Find indices of elements greater than 10
        df=df.to_numpy()
        true_instances = np.where(df ==True)[1]
        #print(true_instances)
        false_instances = np.where(df ==False)[1]
        for i in true_instances:
           df[:,i]=1 
        for i in false_instances:
            df[:,i]=0
        #print(df)
        # Using shape to get the size
        rows, columns = df.shape
        print(f"Number of rows: {rows}, Number of columns: {columns}")
        X=scaler.transform(df)
        y_pred=model.predict(X)
        print(y_pred)
        new_df=pd.DataFrame(y_pred, columns=['Status'])
        new_df=new_df.replace({'Y':'Approved', 'N':'Rejected'})
        message=('Your status is{}'.format(new_df))
        print(new_df)
        return message



@api_view(['GET'])
def prediction(request):
    data=request.data
    print(data)
    df = dataPreprocessing(data=request.data)
    message= predictions(df)
    return Response(message)

    

