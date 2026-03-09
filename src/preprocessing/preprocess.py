import pandas as pd
from pathlib import Path


def preprocess_data(path: str):
    df = pd.read_csv(path)

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    print("=== Head ===")
    print(df.head())

    print("\n=== Data types ===")
    print(df.dtypes)

    print("\n=== Missing values ===")
    print(df.isnull().sum())

    print("\n=== Summary statistics ===")
    print(df.describe())

    return df


if __name__ == "__main__":
    data_path = Path("data/sample_power.csv")
    preprocess_data(data_path)