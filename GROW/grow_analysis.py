"""
GROW Retail Analytics
Run from the GROW folder:
    python grow_analysis.py dataset/samplesuperstore.csv

Requirements:
    pip install pandas matplotlib

Outputs:
    grow_monthly_trend.png
    grow_category_profit.png
"""
import sys

import matplotlib.pyplot as plt
import pandas as pd


input_file = sys.argv[1] if len(sys.argv) > 1 else "dataset/samplesuperstore.csv"
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

# Monthly sales trend
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month", as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum")
)
plt.figure(figsize=(11, 5))
plt.plot(monthly["Month"], monthly["Sales"], marker="o", label="Sales")
plt.xticks(rotation=90)
plt.title("GROW: Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("grow_monthly_trend.png", dpi=160)
plt.close()

# Profit by sub-category: investigate low-profit areas; do not infer causation
subcat = df.groupby("Sub-Category", as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum")
)
subcat = subcat.sort_values("Profit")
plt.figure(figsize=(10, 6))
plt.barh(subcat["Sub-Category"], subcat["Profit"])
plt.title("GROW: Profit by Sub-Category")
plt.xlabel("Profit")
plt.tight_layout()
plt.savefig("grow_category_profit.png", dpi=160)
plt.close()

print("\nCharts saved. Interpret results in context; association is not proof of causation.")
