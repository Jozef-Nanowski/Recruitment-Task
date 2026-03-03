import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    if not re.match(r'^[a-zA-Z_]+$', str(new_column)):
        return pandas.DataFrame([])
    for col in df.columns:
        if not re.match(r'^[a-zA-Z_]+$', str(col)):
            return pandas.DataFrame([])
    if not re.match(r'^[a-zA-Z0-9_\+\-\*\s]+$', role):
        return pandas.DataFrame([])
    words = re.findall(r'[a-zA-Z_]+', role)
    for word in words:
        if word not in df.columns:
            return pandas.DataFrame([])
    try:
        result_df = df.copy()
        result_df[new_column] = result_df.eval(role)
        return result_df
    except Exception:
        return pandas.DataFrame([])
