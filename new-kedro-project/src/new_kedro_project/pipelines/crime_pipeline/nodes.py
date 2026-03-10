"""
This is a boilerplate pipeline 'crime_pipeline'
generated using Kedro 1.2.0
"""
import pandas as pd
import requests
from datetime import datetime


def fetch_data(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    return df


def validate_data(df: pd.DataFrame, min_rows: int, required_columns: list):
    if df.empty:
        raise ValueError("Dataset is empty")

    if len(df) < min_rows:
        raise ValueError("Dataset has too few rows")

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    return df


def clean_transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    df = df.dropna(how="all")

    df = df.drop_duplicates()

    df.columns = [c.lower().replace(" ", "_") for c in df.columns]

    missing = [c for c in ["id",'case_number','primary_type','date'] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df
# def clean_transform(df: pd.DataFrame) -> pd.DataFrame:
#
#     df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
#
#     df = df.dropna(how="all")
#     df = df.replace(r"^\s*$", pd.NA, regex=True)
#     df = df.drop_duplicates()
#
#     # tylko potrzebne kolumny
#     keep_columns = [
#         "id",
#         "case_number",
#         "date",
#         "primary_type",
#         "description",
#         "location_description",
#         "arrest",
#         "domestic",
#         "district",
#         "year"
#     ]
#
#     existing = [c for c in keep_columns if c in df.columns]
#     df = df[existing]
#
#     df = df.reset_index(drop=True)
#
#     return df


def feature_or_aggregate(df: pd.DataFrame, top_k: int) -> pd.DataFrame:
    result = (
        df.groupby("primary_type")
        .size()
        .reset_index(name="crime_count")
        .sort_values("crime_count", ascending=False)
        .head(top_k)
    )

    return result


def generate_report(df: pd.DataFrame) -> dict:
    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "generated_at": datetime.now().isoformat(),
    }

    return report