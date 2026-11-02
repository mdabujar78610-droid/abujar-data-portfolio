"""
GROW Retail Analytics
Run from the repository root:
    python GROW/grow_analysis.py GROW/dataset/samplesuperstore.csv

Requirement:
    pip install pandas

This script performs data-quality checks and summary analysis.
The Tableau workbook is the project's primary dashboard.
"""
import sys
import pandas as pd

input_file = sys.argv[1] if len(sys.argv) > 1 else "GROW/dataset/samplesuperstore.csv"
df = pd.read_csv(input_file)
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Data quality checks
print("Rows, columns:", df.shape)
print("Missing cells:", int(df.isna().sum().sum()))
print("Exact duplicate rows:", int(df.duplicated().sum()))
print("Duplicate Row IDs:", int(df["Row ID"].duplicated().sum()))
print("Ship-before-order rows:", int((df["Ship Date"] < df["Order Date"]).sum()))

# Business KPIs
sales = df["Sales"].sum()
profit = df["Profit"].sum()
print(f"Total sales: {sales:,.2f}")
print(f"Total profit: {profit:,.2f}")
print(f"Profit margin: {profit / sales:.2%}")
print("Unique orders:", df["Order ID"].nunique())
print("Unique customers:", df["Customer ID"].nunique())
print("Negative-profit line items:", int((df["Profit"] < 0).sum()))

# Category and region analysis
category = df.groupby("Category", as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum")
)
category["Profit Margin %"] = category["Profit"] / category["Sales"] * 100
print("\nCategory summary:\n", category.sort_values("Sales", ascending=False).to_string(index=False))

region = df.groupby("Region", as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum")
)
print("\nRegion summary:\n", region.sort_values("Profit", ascending=False).to_string(index=False))

print("\nAnalysis complete. Use the Tableau workbook for dashboard visuals.")
