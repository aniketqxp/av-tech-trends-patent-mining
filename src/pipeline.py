from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from .data_loader import load_jsonl

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def load_patent_dataframe(filename: str = "av_patentdata.jsonl") -> pd.DataFrame:
    """Load the curated patent dataset into a pandas DataFrame."""
    file_path = DATA_DIR / filename
    records = list(load_jsonl(file_path))
    return pd.DataFrame(records)


def build_text_corpus(df: pd.DataFrame, fields: Iterable[str] | None = None) -> pd.Series:
    """Build a single text corpus column from selected patent fields."""
    if fields is None:
        fields = ["invention_title_text", "abstract_text", "claims"]

    def join_fields(row: pd.Series) -> str:
        parts = [str(row[field]).strip() for field in fields if pd.notna(row.get(field)) and str(row[field]).strip()]
        return " \n ".join(parts)

    return df.apply(join_fields, axis=1)


def normalize_publication_dates(df: pd.DataFrame, column: str = "date_published") -> pd.DataFrame:
    """Ensure publication dates are datetime objects and add year/month columns."""
    df = df.copy()
    df[column] = pd.to_datetime(df[column], errors="coerce")
    df["year"] = df[column].dt.year
    df["month"] = df[column].dt.month
    return df


def save_dataframe_csv(df: pd.DataFrame, filename: str = "patent_dataset.csv") -> Path:
    """Save the DataFrame to a CSV file in the data directory."""
    destination = DATA_DIR / filename
    df.to_csv(destination, index=False)
    return destination


if __name__ == "__main__":
    df = load_patent_dataframe()
    corpus = build_text_corpus(df)
    df = normalize_publication_dates(df)
    csv_path = save_dataframe_csv(df)
    print(f"Loaded {len(df)} patents and saved CSV to {csv_path}")
