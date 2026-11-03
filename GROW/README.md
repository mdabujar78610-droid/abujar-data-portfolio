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

## Tools
- **Excel:** KPI summaries, formulas, analysis tables, and charts.
- **SQL:** KPI, category, regional, sub-category, discount, monthly, and data-quality queries.
- **Python:** data preparation, checks, and KPI analysis with Pandas.
- **Tableau:** worksheets and dashboard for visual analysis.

## Project Files
- [Excel workbook](GROW_Analytics_Workbook.xlsx)
- [Python analysis](grow_analysis.py)
- [SQL analysis](sql/grow_analysis.sql)
- [Sample dataset](dataset/samplesuperstore.csv)
- [Tableau workbook](tableau/GROW_Tableau_Dashboard.twb)

## Notes
- Sales and Profit in the Tableau visuals are shown in USD ($).
- PNGs are static previews; the TWB file is the editable Tableau workbook.
- Findings are descriptive and must not be presented as verified company performance.

---
*Portfolio project by Mohammad Abuzar.*
