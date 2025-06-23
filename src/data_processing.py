# src/data_processing.py

import pandas as pd
import os
from typing import Literal


def load_raw_data(
    data_type: Literal["resident", "floating", "estimated_sales"],
    raw_folder: str = "data/raw",
    encoding: str = "cp949",
) -> pd.DataFrame:
    """
    'data/raw/'에서 data_type에 해당하는 키워드를 포함한 CSV 파일을 찾아 읽어옵니다.
    - data_type "resident"        -> 파일명에 '상주인구-상권' 포함
    - data_type "floating"        -> 파일명에 '길단위인구-상권' 포함
    - data_type "estimated_sales" -> 파일명에 '추정매출-상권' 포함
    """
    keyword_map = {
        "resident": "상주인구-상권",
        "floating": "길단위인구-상권",
        "estimated_sales": "추정매출-상권",
    }
    keyword = keyword_map[data_type]
    # raw_folder 에서 해당 키워드가 포함된 .csv 파일 검색
    candidates = [
        fname
        for fname in os.listdir(raw_folder)
        if keyword in fname and fname.lower().endswith(".csv")
    ]
    if not candidates:
        raise FileNotFoundError(f"No CSV found in '{raw_folder}' for '{data_type}'")
    # 첫 번째 발견 파일 로드
    file_path = os.path.join(raw_folder, candidates[0])
    df = pd.read_csv(file_path, encoding=encoding)
    return df


def aggregate_by_code(
    df: pd.DataFrame, code_col: str, value_col: str, suffix: str = "2024"
) -> pd.DataFrame:
    """
    df를 code_col 기준으로 합계를 구한 뒤
    [code_col, f"{value_col}_{suffix}"] 형태의 DataFrame을 반환합니다.
    """
    agg = df.groupby(code_col)[value_col].sum().reset_index()
    agg.columns = [code_col, f"{value_col}_{suffix}"]
    return agg
