import pandas as pd
from pathlib import Path

def load_csv(file_path):
    file_path=Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError("CSV file not found!")
    if file_path.suffix.lower() != ".csv":
        raise ValueError("Please provide a CSV file!")
    data=pd.read_csv(file_path)
    return data