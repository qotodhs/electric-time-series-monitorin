import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_prediction(path: str):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)

    df["predicted_power_usage"] = df["power_usage"].shift(1)
    result_df = df.dropna().copy()

    plt.figure(figsize=(10, 5))
    plt.plot(result_df["timestamp"], result_df["power_usage"], label="Actual")
    plt.plot(result_df["timestamp"], result_df["predicted_power_usage"], label="Predicted")

    plt.xlabel("Timestamp")
    plt.ylabel("Power Usage")
    plt.title("Actual vs Predicted Power Usage")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    data_path = Path("data/sample_power.csv")
    plot_prediction(data_path)