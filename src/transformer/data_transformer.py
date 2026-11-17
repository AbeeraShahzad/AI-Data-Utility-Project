#Converts the data in a useful format
import pandas as pd
import numpy as np
#Convert data types
def convert_data_type(data,column,data_type):
    transformed_data=data.copy()
    transformed_data[column]=transformed_data[column].astype(data_type)
    return transformed_data
#Encode Categorial data
def encode_categorial_data(data,column):
    transformed_data=data.copy()
    transformed_data=pd.get_dummies(transformed_data,columns=[column],dtype="int")
    return transformed_data
#Data Normalization
def normalize_data(data,column):
    transformed_data=data.copy()
    maximum=transformed_data[column].max()
    minimum=transformed_data[column].min()
    if maximum==minimum:
        transformed_data[column]=0
    else:
        transformed_data[column]=(transformed_data[column]-minimum)/(maximum-minimum)

    return transformed_data
#Standardize numerical data
def standardize_data(data,column):
    transformed_data=data.copy()
    mean=transformed_data[column].mean()
    std=transformed_data[column].std()
    if std==0:
        transformed_data[column]=0
    else:
        transformed_data[column]=(transformed_data[column]-mean)/std
    return transformed_data
#Create New Feature
def create_average_feature(data,column1,column2,new_column):
    transformed_data=data.copy()
    transformed_data[new_column]=transformed_data[column1]+transformed_data[column2]/2
    return transformed_data
#Feature binning
def bin_numerical_data(data,column,bins,labels):
    transformed_data=data.copy()
    transformed_data[column+"_group"]=pd.cut(transformed_data[column],
                                            bins=bins,labels=labels)
    return transformed_data
#Log Transformation
def log_transform(data,column):
    transformed_data=data.copy()
    if(transformed_data[column]<=-1).any():
        raise ValueError("Values must be greater than -1!")
    transformed_data[column]=np.log1p(transformed_data[column])
    return transformed_data
#Round Numerical Values
def round_numerical_data(data,column,decimals):
    transformed_data=data.copy()
    transformed_data[column]=transformed_data[column].round(decimals)
    return transformed_data
