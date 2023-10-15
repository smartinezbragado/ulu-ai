import pandas as pd

class InvalidFormatError(Exception):
    pass

def read_file_as_dataframe(path: str) -> pd.DataFrame:
    """Given a file path to an excel or csv file returns a pandas dataframe"""
    if path.endswith('.csv'):
        return pd.read_csv(path)
    elif path.endswith('.xlsx'):
        return pd.read_excel(path)
    else:
        raise InvalidFormatError("Invalid file format")
    