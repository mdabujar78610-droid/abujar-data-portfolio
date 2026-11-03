# GROW — Retail Sales & Profitability Analysis

**Portfolio case study** · Excel · SQL · Python · Tableau

## Overview
GROW is a retail analytics case study using the Sample Superstore dataset. It explores sales, profit, profit margin, category and regional performance, sub-category profitability, monthly trends, and data quality.

> **Dataset disclosure:** Sample Superstore is sample/learning data, not verified company records. Findings describe only this dataset.

## Tableau Dashboard
![GROW Tableau dashboard](dashboard/grow_dashboard.png)

[Dashboard preview](dashboard/grow_dashboard.png) · [Editable Tableau workbook](tableau/GROW_Tableau_Dashboard.twb)

## Chart Gallery
### Sales by Category
![Sales by Category](charts/sales_by_category.png)

### Profit by Sub-Category
![Profit by Sub-Category](charts/profit_by_sub_category.png)

### Profit by Region
![Profit by Region](charts/profit_by_region.png)

### Monthly Sales & Profit Trend
![Monthly Sales and Profit Trend](charts/monthly_sales_profit_trend.png)

## Key Performance Indicators
| Metric | Result |
|---|---:|
| Total Sales | $2,326,534.35 |
| Total Profit | $292,296.81 |
| Profit Margin | 12.56% |
| Distinct Orders | 5,111 |
| Distinct Customers | 804 |
| Negative-Profit Line Items | 1,901 |

## Key Findings
- Technology has the highest sales among the three categories.
- Tables is the lowest-profit sub-category and has a negative total profit.
- The West region records the highest profit among the four regions.

## Tools and analysis
- **Excel:** KPI summaries, formulas, PivotTables, analysis tables, and charts.
- **SQL:** overall KPIs, category and regional comparisons, sub-category profitability, discount analysis, monthly trends, and data-quality checks.
- **Python:** data-quality checks, KPI calculations, and category/region summaries with Pandas.
- **Tableau:** worksheets, calculated fields, interactive highlight actions, and dashboard visualization.

## Run the Python analysis
From the repository root:

```bash
python -m pip install -r GROW/requirements.txt
python GROW/grow_analysis.py GROW/dataset/samplesuperstore.csv
```

The script prints data-quality checks and business summaries in the terminal.

## Run the SQL analysis
The SQL file is written for SQLite and expects a table named `superstore`.

1. Create a SQLite database.
2. Import `dataset/samplesuperstore.csv` into a table named `superstore` (keep the original column names, including spaces).
3. Open [sql/grow_analysis.sql](sql/grow_analysis.sql) in a SQLite-compatible SQL editor.
4. Run the queries section by section and compare the KPI results with the project summary.

For example, with DB Browser for SQLite: create/open a database, use **File → Import → Table from CSV**, select the dataset, and set the table name to `superstore`.

## Open the Tableau workbook
1. Open [tableau/GROW_Tableau_Dashboard.twb](tableau/GROW_Tableau_Dashboard.twb) in Tableau Desktop.
2. If prompted, reconnect the data source to `dataset/samplesuperstore.csv`.
3. Refresh the data and verify that the worksheets, filters, and dashboard load correctly.

See [the Tableau-specific guide](tableau/README.md) for workbook details.

## Project files
- [Excel workbook](GROW_Analytics_Workbook.xlsx)
- [Python analysis](grow_analysis.py)
- [Python requirements](requirements.txt)
- [SQL analysis](sql/grow_analysis.sql)
- [Sample dataset](dataset/samplesuperstore.csv)
- [Tableau workbook](tableau/GROW_Tableau_Dashboard.twb)

## Notes
- Sales and Profit are reported in USD ($) in this project summary; keep workbook number formats consistent.
- PNGs are static previews; the TWB file is the editable Tableau workbook.
- Findings are descriptive and must not be presented as verified company performance.

---
*Portfolio project by Mohammad Abuzar.*
