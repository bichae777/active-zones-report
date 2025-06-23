# src/activity_flags.py

import pandas as pd
from typing import List


def generate_activity_flags(
    df: pd.DataFrame, code_col: str, metric_cols: List[str]
) -> pd.DataFrame:
    """
    Q3(75%), Q90(90%), Median 기준 high25/high10/high50 플래그와
    is_active_25, is_active_10, is_active_50 컬럼을 추가합니다.
    """
    # 1) 기준값 계산
    qs = {
        col: {
            "q75": df[col].quantile(0.75),
            "q90": df[col].quantile(0.90),
            "med": df[col].median(),
        }
        for col in metric_cols
    }

    # 2) 플래그 생성
    for col in metric_cols:
        df[f"{col}_high25"] = df[col] >= qs[col]["q75"]
        df[f"{col}_high10"] = df[col] >= qs[col]["q90"]
        df[f"{col}_high50"] = df[col] >= qs[col]["med"]

    # 3) 활성 상권 판단
    df["active_25_cnt"] = df[[f"{c}_high25" for c in metric_cols]].sum(axis=1)
    df["is_active_25"] = df["active_25_cnt"] >= 2

    df["active_10_cnt"] = df[[f"{c}_high10" for c in metric_cols]].sum(axis=1)
    df["is_active_10"] = df["active_10_cnt"] >= 2

    df["is_active_50"] = df[[f"{c}_high50" for c in metric_cols]].all(axis=1)

    return df
