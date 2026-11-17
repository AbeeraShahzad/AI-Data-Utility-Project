#useful statistical information nikaalna hai
#mean,median,mode,max,min,sum,standard deviation
#Calculate Mean
def calculate_mean(data,column):
    result=data[column].mean()
    return result
#Calculate Median
def calculate_median(data,column):
    result=data[column].median()
    return result
#Calculate Mode
def calculate_mode(data,column):
    result=data[column].mode()
    return result
#Find Maximum
def find_max(data,column):
    result=data[column].max()
    return result
#Find Minimum
def find_min(data,column):
    result=data[column].min()
    return result
#Find Sum
def calculate_sum(data,column):
    result=data[column].sum()
    return result
#Find Standard_deviation
def calculate_std(data,column):
    result=data[column].std()
    return result