# GROW — Retail Sales & Profitability Analysis

**Junior Data Analyst portfolio project | Excel • SQL • Python • Tableau**

## Project overview
GROW is a simulated retail-business case study built with the Sample Superstore dataset. The project explores sales, profit, category and regional performance, sub-category profitability, discount patterns, and data quality.

> **Dataset note:** This is sample data, not verified data from a real GROW company. The source dates run from 3 Jan 2023 through 30 Dec 2026, so validate the date range before presenting it as historical performance.

## Dataset and quality checks
- 10,194 transaction rows and 21 columns
- 5,111 distinct orders and 804 distinct customers
- The supplied Python checks reported no missing cells, exact duplicate rows, duplicate Row IDs, or ship-before-order records

## Key results from the supplied sample data
- **Total sales:** $2,326,534.35
- **Total profit:** $292,296.81
- **Profit margin:** 12.56%
- **Negative-profit line items:** 1,901 (18.65%)
- **Highest category sales:** Technology — $839,893.28
- **Lowest sub-category profit:** Tables — -$17,753.21
- **Lowest regional profit:** Central — $39,865.31

These are descriptive results from the sample file, not causal conclusions or claims about an actual company.

## Tools and analysis
- **Excel:** KPI summary, data checks, analysis tables, and chart gallery.
- **SQL:** reusable queries for sales, profit, category, region, and sub-category analysis.
- **Python:** Pandas data-quality checks, KPI calculations, category/region summaries, and Matplotlib chart generation.
- **Tableau:** dashboard workbook with KPI views, monthly trend, category/region/sub-category analysis, and three highlight actions.

## Run the Python analysis
From the repository root:

```bash
pip install pandas matplotlib
python GROW/grow_analysis.py GROW/dataset/samplesuperstore.csv
```

The script prints data-quality checks and business KPIs, then saves:
- `grow_monthly_trend.png`
- `grow_category_profit.png`

## Dashboard preview and chart gallery
![GROW dashboard preview](charts/GROW_Dashboard_Preview.svg)

- [Sales by Category — Bar Chart](charts/01_sales_by_category_bar.svg)
- [Sales Mix by Category — Pie Chart](charts/02_sales_mix_pie.svg)
- [Monthly Sales & Profit — Line Chart](charts/03_monthly_sales_profit_line.svg)
- [Profit by Region — Bar Chart](charts/04_profit_by_region_bar.svg)
- [Profit by Sub-category — Bar Chart](charts/05_profit_by_subcategory_bar.svg)

## Tableau workbook review
The supplied Tableau workbook contains **1 dashboard, 12 worksheets, and 3 highlight actions**. Its calculated fields include:
- Profit Margin: `SUM([Profit]) / SUM([Sales])`
- Orders: `COUNTD([Order ID])`
- Negative Profit count: `SUM(IF [Profit] < 0 THEN 1 ELSE 0 END)`

**Data connection:** The original workbook referred to a local Windows folder. The adjusted copy uses a repository-relative `dataset` folder; keep the workbook inside `GROW/` beside that folder. If Tableau still prompts for the source, connect it to [`dataset/samplesuperstore.csv`](dataset/samplesuperstore.csv).

**Currency review:** The workbook's Sales and Profit views use the ₹ symbol, while the supplied KPI summary above is expressed in US dollars. Confirm the intended currency and make the display consistent before publishing screenshots or presenting the figures.

**Workbook file:** The Tableau workbook itself is not yet committed to this repository. Add `GROW_Tableau_Dashboard.twb` to this folder to make it available to visitors.
