import pandas as pd 
import numpy as np 

def get_dataset(size):
    # create fake Dataset
    df = pd.DataFrame()
    df["size"] = np.random.choice(["big", "medium", "small"], size)
    df["age"] = np.random.randint(1, 50, size)
    df["team"] = np.random.choice(["red", "blue", "yellow", "green"], size)
    df["win"] = np.random.choice(["yes", "no"], size)
    dates = pd.date_range("2020-01-01", "2022-12-31")
    df["date"] = np.random.choice(dates, size)
    df["prob"] = np.random.uniform(0, 1, size)
    return df

def set_dtypes(df):
    df["size"] = df["size"].astype("category")
    df["age"] = df["age"].astype("int16")
    df["team"] = df["team"].astype("category")
    df["win"] = df["win"].astype("bool")
    dates = pd.date_range("2020-01-01", "2022-12-31")
    df["prob"] = df["prob"].astype("float16")
    return df