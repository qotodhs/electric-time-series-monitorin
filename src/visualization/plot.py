import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_power_usage(path: str):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["power_usage"])
    plt.xlabel("Timestamp")
    plt.ylabel("Power Usage")
    plt.title("Power Usage Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    data_path = Path("data/sample_power.csv")
    plot_power_usage(data_path)