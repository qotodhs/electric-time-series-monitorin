import pandas as pd
from pathlib import Path


def train_baseline_model(path: str):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)

    # 이전 시점 값을 다음 시점 예측값으로 사용하는 baseline
    df["predicted_power_usage"] = df["power_usage"].shift(1)

    # 첫 행은 이전 값이 없으므로 제거
    result_df = df.dropna().copy()

    # 절대 오차 계산
    result_df["absolute_error"] = (
        result_df["power_usage"] - result_df["predicted_power_usage"]
    ).abs()

    mae = result_df["absolute_error"].mean()

    print("=== Prediction Result ===")
    print(result_df[["timestamp", "power_usage", "predicted_power_usage", "absolute_error"]])

    print(f"\nMAE: {mae:.4f}")

    return result_df, mae


if __name__ == "__main__":
    data_path = Path("data/sample_power.csv")
    train_baseline_model(data_path)