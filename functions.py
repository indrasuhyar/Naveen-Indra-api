import pandas as pd

def get_distinct_count(df: pd.DataFrame):
    return df.nunique()

def get_missing_count(df: pd.DataFrame):
    return df.isnull().sum()

def get_missing_percentage(df: pd.DataFrame):
    return (df.isnull().sum() / len(df)) * 100

def get_distinct_percentage(df: pd.DataFrame):
    return (df.nunique() / len(df)) * 100
