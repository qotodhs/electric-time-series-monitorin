import pandas as pd
from pathlib import Path


def load_data(path: str):
    df = pd.read_csv(path)
    print(df.head())
    return df


if __name__ == "__main__":
    data_path = Path("data/sample_power.csv")
    load_data(data_path)