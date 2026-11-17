import pandas as pd
from pathlib import Path

from altair.datasets import data
#Export data to CSV
def export_to_csv(data,file_path):
    file_path=Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(file_path,index=False)
    return file_path
#Export to Excel
def export_to_excel(data,file_path):
    file_path=Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_excel(file_path,index=False)
    return file_path
#Export to JSON
def export_to_json(data,file_path):
    file_path=Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_json(file_path,orient='records')
    return file_path
#Export to TXT
def export_to_txt(data,file_path):
    file_path=Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(file_path,index=False)
    return file_path
