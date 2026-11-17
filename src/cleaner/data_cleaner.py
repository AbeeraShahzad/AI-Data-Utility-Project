#Remove Duplicates
def remove_duplicates(data):
    cleaned_data=data.copy()
    cleaned_data=cleaned_data.drop_duplicates()
    return cleaned_data
#Fill missing values
def fill_missing_values(data,column,value):
    cleaned_data=data.copy()
    cleaned_data=cleaned_data.fillna(value)
    return cleaned_data
#Remove completely empty rows
def remove_empty_rows(data):
    cleaned_data=data.copy()
    cleaned_data=cleaned_data.dropna(how="all")
    return cleaned_data
#Standardize column names
def clean_column_names(data):
    cleaned_data=data.copy()
    cleaned_data.columns=(
        cleaned_data.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return cleaned_data
