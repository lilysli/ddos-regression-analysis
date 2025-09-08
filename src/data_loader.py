import pandas as pd

def uni_load_flow_data(csv_path):
    """
    Loads all columns from rows labeled 'DDoS'.
    """
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    df_ddos = df[df['Label'] == 'DDoS']

    return df_ddos

def load_logistic_regression_data(csv_path):
    """
    Loads all columns from rows labeled 'DDoS'.
    """
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    return df