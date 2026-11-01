"""Recreated, reusable Users Data Report starter.
Usage: python src/users_data_report.py path/to/input.csv --output outputs
Supports CSV and Excel inputs. Does not upload data to any AI service.
"""
from pathlib import Path
import argparse
import re
import pandas as pd
import matplotlib.pyplot as plt

def safe_name(value):
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", str(value)).strip("_")[:50] or "column"

def load_data(path):
    path = Path(path)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError("Supported files: .csv, .xlsx, .xls")

def main():
    parser = argparse.ArgumentParser(description="Clean and summarize a user-supplied dataset.")
    parser.add_argument("input", help="Path to a CSV or Excel file")
    parser.add_argument("--output", default="outputs", help="Output folder (default: outputs)")
    args = parser.parse_args()

    out = Path(args.output)
    charts = out / "charts"
    charts.mkdir(parents=True, exist_ok=True)
    df = load_data(args.input)
    if df.empty:
        raise ValueError("The input file has no data rows.")

    original_rows, original_cols = df.shape
    df.columns = [str(c).strip() for c in df.columns]
    df = df.dropna(how="all").drop_duplicates().copy()

    # Trim text fields; preserve missing values.
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    missing = df.isna().sum().rename("missing_count").to_frame()
    missing["missing_percent"] = (missing["missing_count"] / max(len(df), 1) * 100).round(2)
    missing.to_csv(out / "missing_values.csv")

    numeric = df.select_dtypes(include="number")
    categorical = df.select_dtypes(include=["object", "string", "category"])

    kpis = pd.DataFrame([
        ("Rows before cleaning", original_rows),
        ("Columns", original_cols),
        ("Rows after removing blank rows and exact duplicates", len(df)),
        ("Exact duplicate rows removed", original_rows - len(df)),
        ("Missing cells after basic cleaning", int(df.isna().sum().sum())),
        ("Numeric columns", len(numeric.columns)),
        ("Categorical columns", len(categorical.columns)),
    ], columns=["metric", "value"])
    kpis.to_csv(out / "kpi_summary.csv", index=False)

    if not numeric.empty:
        numeric.describe().T.to_csv(out / "numeric_summary.csv")
        for col in numeric.columns[:8]:
            values = df[col].dropna()
            if not values.empty:
                plt.figure(figsize=(8, 4))
                plt.hist(values, bins=20)
                plt.title(f"Distribution: {col}")
                plt.xlabel(col)
                plt.ylabel("Frequency")
                plt.tight_layout()
                plt.savefig(charts / f"{safe_name(col)}_distribution.png", dpi=140)
                plt.close()

    for col in categorical.columns[:5]:
        counts = df[col].fillna("(Missing)").astype(str).value_counts().head(10)
        if not counts.empty:
            plt.figure(figsize=(9, 4))
            counts.sort_values().plot(kind="barh")
            plt.title(f"Top values: {col}")
            plt.xlabel("Count")
            plt.ylabel(col)
            plt.tight_layout()
            plt.savefig(charts / f"{safe_name(col)}_top_values.png", dpi=140)
            plt.close()

    cleaned_path = out / "cleaned_data.csv"
    df.to_csv(cleaned_path, index=False)
    print(f"Completed. Cleaned data: {cleaned_path}")
    print(f"KPIs: {out / 'kpi_summary.csv'}")
    print(f"Charts: {charts}")
    print("Review data types and business rules manually before using results.")
    print("No AI-generated conclusions are produced by this local script.")

if __name__ == "__main__":
    main()
