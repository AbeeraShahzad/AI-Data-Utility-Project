#Get Function Shape
from altair.datasets import data
def get_dataset_shape(data):
    return data.shape
#Get column names
def get_column_names(data):
    return data.columns.tolist()
#Display dataset information
def get_dataset_info(data):
    data.info()
#check missing values
def get_missing_values(data):
    return data.isnull().sum()
#Count duplicate records
def get_duplicate_count(data):
    return data.duplicated().sum()
#Get data types
def get_data_types(data):
    return data.dtypes
