AI Data Utility Project

Overview

AI Data Utility is a Python-based data processing project designed to load, inspect, clean, analyze, transform, and export datasets efficiently.

Features

1. Data Loading

- Load CSV datasets.
- Validate file existence.
- Validate file format.

2. Data Inspection

- Dataset shape
- Column names
- Dataset information
- Missing values
- Duplicate records
- Data types

3. Data Cleaning

- Remove duplicate records
- Fill missing values
- Remove empty rows
- Standardize column names

4. Data Analysis

- Mean
- Median
- Mode
- Maximum and minimum
- Sum
- Standard deviation

5. Data Transformation

- Data type conversion
- Categorical encoding
- Normalization
- Standardization
- Feature creation
- Feature binning
- Log transformation
- Numerical rounding

6. Data Exporting

- CSV
- Excel
- JSON
- TXT

Technologies Used

- Python
- Pandas
- NumPy
- Pytest

Project Structure

AI_Data_Utility_Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
├── src/
│   ├── loader/
│   ├── inspector/
│   ├── cleaner/
│   ├── analyzer/
│   ├── transformer/
│   └── exporter/
│
├── tests/
├── main.py
└── README.md

How to Run

1. Clone or download the project.
2. Install the required dependencies.
3. Place your CSV dataset inside "data/raw/".
4. Run "main.py".

Output

The processed dataset is exported into CSV, Excel, JSON, and TXT formats inside "data/processed/".
