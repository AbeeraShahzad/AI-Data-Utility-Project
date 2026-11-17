import pandas as pd
from src.cleaner.data_cleaner import(
    remove_duplicates,
    fill_missing_values,
    remove_empty_rows,
    clean_column_names
)
#Remove Duplicates
def test_remove_duplicates():
    data=pd.DataFrame({
        "name":["Ali","Sara","Ali"],
        "age":[20,22,20]
    })
    result = remove_duplicates(data)
    assert len(result) == 2

#Fillin missing values
def test_fill_missing_values():
    data=pd.DataFrame({
        "age":[20,None,25]
    })
    result = fill_missing_values(data,"age",0)
    assert result["age"].isnull().sum() == 0
    assert result["age"].iloc[1] == 0

#Remove Empty rows
def test_remove_empty_rows():
    data=pd.DataFrame({
        "Name":["Ali",None,"Sara"],
        "age":[20,None,22]
    })
    result=remove_empty_rows(data)
    assert len(result) == 2
#Clean Column Names
def test_clean_column_names():
    data=pd.DataFrame({
        "Student name":["Ali","Sara"],
        "Student age":[20,22]
    })
    result = clean_column_names(data)
    assert list(result.columns)==["student_name","student_age"]