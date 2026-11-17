from pathlib import Path
from src.loader.data_loader import load_csv
from src.inspector.data_inspector import(
    get_dataset_shape,
    get_column_names,
    get_dataset_info,
    get_missing_values,
    get_duplicate_count,
    get_data_types
)
from src.cleaner.data_cleaner import (
    remove_duplicates,
    fill_missing_values,
    remove_empty_rows,
    clean_column_names
)
from src.analyzer.data_analyzer import(
    calculate_mean,
    calculate_median,
    calculate_mode,
    find_max,
    find_min,
    calculate_sum,
    calculate_std,

)
from src.transformer.data_transformer import (
    convert_data_type,
    encode_categorial_data,
    normalize_data,
    standardize_data,
    create_average_feature,
    bin_numerical_data,
    log_transform,
    round_numerical_data
)
from src.exporter.data_exporter import (
    export_to_csv,
    export_to_excel,
    export_to_json,
    export_to_txt,
)
PROJECT_DIR=Path(__file__).resolve().parent
file_path=PROJECT_DIR/"data"/"raw"/"student_academic_success.csv"
print("File_Path:",repr(file_path))
print("File Extension:",
      repr(file_path.suffix))
print("File Exists:", file_path.exists())
students_data=load_csv(file_path)
print("Dataset Loaded Successfully!")
print(students_data)
                                               #DATA INSPECTION
print("\n========DATA INSPECTION=========")
# Shape
print("\nDataset Shape:")
print(get_dataset_shape(students_data))
#Column Names
print("\nColumns Names:")
print(get_column_names(students_data))
#Information
print("\nDataset Info:")
get_dataset_info(students_data)
#Missing Value
print("\nMissing Values:")
print(get_missing_values(students_data))
#Duplicate Records
print("\nDuplicate Records:")
print(get_duplicate_count(students_data))
#Data Types
print("\nData Types:")
print(get_data_types(students_data))

                                            #DATA CLEANING
print("\n========DATA CLEANING=========")
#Create a working copy
cleaned_data=students_data.copy()
#Remove duplicate records
cleaned_data=remove_duplicates(cleaned_data)
print("\nDuplicate Records Removed!")
#Remove Completely Empty Rows
cleaned_data=remove_empty_rows(cleaned_data)
print("\nEmpty Rows Removed!")
#Clean column names
cleaned_data=clean_column_names(cleaned_data)
print("\nColumn Names Standardized!")
#Display cleaned Dataset
print("\nCleaned Dataset")
print(cleaned_data.head())

                                             #DATA ANALYZING
print("\n========DATA ANALYZING=========")
print("\nAvailable Columns:")
print(cleaned_data.columns.tolist())
column="age"
print("Mean:",calculate_mean(cleaned_data,column))
print("Median:",calculate_median(cleaned_data,column))
print("Mode:",calculate_mode(cleaned_data,column))
print("Maximum:",find_max(cleaned_data,column))
print("Minimum:",find_min(cleaned_data,column))
print("Sum:",calculate_sum(cleaned_data,column))
print("Standard Deviation:",calculate_std(cleaned_data,column))

                                           #DATA TRANSFORMATION
print("\n========DATA TRANSFORMATION=========")
#Valur Transformation
final_data=cleaned_data.copy()
final_data=convert_data_type(final_data,
                                   "gender",
                                   "category"
                                   )
print("\nOriginal Data Types:")
print(cleaned_data["gender"].dtype)
print("\nTransformed Data Type:")
print(final_data["gender"].dtype)
#encoding categorial data
final_data=encode_categorial_data(final_data,
                                   "gender")
print("\nEncode Gender Columns:")
print(final_data.filter(like="gender_").head())
print("\nEncoded Dataset Shape")
print(final_data.shape)
#data normalization
final_data=normalize_data(final_data,"gpa")
print(cleaned_data["gpa"].head())
print("\nNormalized GPA values")
print(final_data["gpa"].head())
#data standardization
final_data=standardize_data(final_data,"gpa")
print("\nOriginal GPA Values:")
print(cleaned_data["gpa"].head())
print("\nStandardized GPA Values")
print(final_data["gpa"].head())
print("\nStandardized GPA Mean:")
print(final_data["gpa"].mean())
#new Feature Creation
final_data=create_average_feature(final_data,"attendance_percentage",
                                    "assignment_completion_rate",
                                    "academic_engagement_score")
print("\nNew Feature: Academic Engagement Score")
print(final_data[[
    "attendance_percentage",
    "assignment_completion_rate",
    "academic_engagement_score"
]].head())
print("\nUpdated Dataset Shape:")
print(final_data.shape)
#binning data
final_data=bin_numerical_data(final_data,
                               "age",
                               4,
                               ["Group 1", "Group 2", "Group 3","Group 4"])
print("\nAge Groups:")
print(final_data[["age","age_group"]].head())
#converting data to logrithemic values
final_data=log_transform(final_data,"study_hours_per_day")
print("\nLog Transformation Study Hours:")
print(final_data["study_hours_per_day"].head())
#round off numerical decimal values
final_data=round_numerical_data(final_data,"gpa",2)
print("\nRounded GPA Values:")
print(final_data["gpa"].head())

final_data=cleaned_data.copy()

                                                #DATA EXPORTING
print("\n=======DATA EXPORTER=======")
#Processed folder path
processed_folder=PROJECT_DIR/"data"/"processed"
#Export CSV
csv_path=export_to_csv(final_data,
                        processed_folder/"cleaned_students.csv")
print("\nCSV File Saved: ",csv_path)
#Export excel
excel_path=export_to_excel(final_data,
                        processed_folder/"cleaned_students.xlsx")
print("\nExcel File Saved: ",excel_path)
#Export json
json_path=export_to_json(final_data,
                        processed_folder/"cleaned_students.json")
print("\nJSON File Saved: ",json_path)
#Export TXT
txt_path=export_to_txt(final_data,
                        processed_folder/"cleaned_students.txt")
print("\nTXT File Saved: ",txt_path)

                                        #DATA DISPLAYING AFTER LOADING
#Display 5 rows
print("\nFirst 5 Rows")
print(students_data.head())
#Display last 5 rows
print("\nSecond 5 Rows")
print(students_data.tail())
#Display number of rows and columns
print("\n Dataset Shape")
print(students_data.shape)
#Display column names
print("\nColumn Names:")
print(students_data.columns)
#Display Dataset information
print("\nDataset Information:")
students_data.info()
#Display statistical summary
print("\nStatistical Summary:")
print(students_data.describe())
