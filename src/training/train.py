import pandas as pd
from pathlib import Path


def train_test_baseline(path: str, test_ratio: float = 0.2):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)

    split_index = int(len(df) * (1 - test_ratio))

    train_df = df.iloc[:split_index].copy()
    test_df = df.iloc[split_index:].copy()

    # baseline: 직전 실제값을 다음 값 예측으로 사용
    df["predicted_power_usage"] = df["power_usage"].shift(1)

    result_df = df.dropna().copy()

    train_result = result_df[result_df["timestamp"].isin(train_df["timestamp"])]
    test_result = result_df[result_df["timestamp"].isin(test_df["timestamp"])]

    train_result["absolute_error"] = (
        train_result["power_usage"] - train_result["predicted_power_usage"]
    ).abs()

    test_result["absolute_error"] = (
        test_result["power_usage"] - test_result["predicted_power_usage"]
    ).abs()

    train_mae = train_result["absolute_error"].mean()
    test_mae = test_result["absolute_error"].mean()

    print("=== Train Result ===")
    print(train_result[["timestamp", "power_usage", "predicted_power_usage", "absolute_error"]])

    print(f"\nTrain MAE: {train_mae:.4f}")

    print("\n=== Test Result ===")
    print(test_result[["timestamp", "power_usage", "predicted_power_usage", "absolute_error"]])

    print(f"\nTest MAE: {test_mae:.4f}")

    return train_result, test_result, train_mae, test_mae


if __name__ == "__main__":
    data_path = Path("data/sample_power.csv")
    train_test_baseline(data_path)