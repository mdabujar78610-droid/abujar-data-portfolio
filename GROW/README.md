# GROW — Retail Sales & Profitability Analysis

**Data analytics portfolio case study** · Excel · SQL · Python · Tableau

## Project Overview

GROW is a retail analytics case study built with the Sample Superstore dataset. The project examines sales, profit, profit margin, category and regional performance, sub-category profitability, monthly trends, and data quality.

> **Dataset note:** This is a sample-data portfolio project, not verified business data from a real company. The results below describe only the supplied dataset.

## Dashboard Preview

![GROW retail sales and profitability dashboard](dashboard/grow_dashboard.png)

[View dashboard image](dashboard/grow_dashboard.png)

## Visual Analysis

### Sales by Category
![Sales by Category](charts/sales_by_category.png)

### Profit by Sub-Category
![Profit by Sub-Category](charts/profit_by_sub_category.png)

### Profit by Region
![Profit by Region](charts/profit_by_region.png)

### Monthly Sales and Profit Trend
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

### Key Observations

- Technology has the highest sales among the three product categories.
- Tables have the lowest sub-category profit and are loss-making in the supplied data.
- The West region records the highest profit among the four regions.
- The monthly chart shows sales and profit movement over the dataset's date range.

These are descriptive observations, not causal conclusions or claims about a real retailer.

## Tools and Workflow

- **Excel:** KPI summaries, data-quality review, category/region/monthly analysis, and charts.
- **SQL:** reusable queries for overall KPIs, category, region, sub-category, discount, monthly trends, and data-quality checks.
- **Python:** data cleaning checks, KPI calculations, and summary analysis using Pandas.
- **Tableau:** dashboard and worksheet-based visual analysis.

## Project Files

| Resource | Link |
|---|---|
| Excel analysis workbook | [GROW_Analytics_Workbook.xlsx](GROW_Analytics_Workbook.xlsx) |
| Python analysis | [grow_analysis.py](grow_analysis.py) |
| SQL analysis | [SQL folder](sql/) |
| Dataset | [Dataset folder](dataset/) |
| Tableau workbook currently published in this repository | [GROW_Tableau_Dashboard.twb](tableau/GROW_Tableau_Dashboard.twb) |
| Tableau folder notes | [Tableau README](tableau/README.md) |

**Tableau update note:** The workbook link above points to the version currently published in this repository. The newly supplied Tableau workbook is not uploaded yet, so this link will be updated after the replacement file is successfully committed.

## Repository Structure

```text
GROW/
├── charts/
├── dashboard/
├── dataset/
├── sql/
├── tableau/
├── GROW_Analytics_Workbook.xlsx
├── GROW_Retail_Sales_&_Profitability.zip
├── grow_analysis.py
└── README.md
```

## Running the Python Analysis

From the repository root:

```bash
pip install pandas
python GROW/grow_analysis.py GROW/dataset/samplesuperstore.csv
```

## Notes and Limitations

- The dataset is sample data; it should not be presented as verified company data.
- The currency shown in the supplied charts and KPI summary is USD ($).
- Discount/profit relationships are descriptive and do not establish causation.
- PNG files are static chart previews; the Tableau workbook is the editable analysis file.
- The supplied dataset's date range is part of the sample data and should not be interpreted as a real company's reporting history.

---

*Portfolio project by Mohammad Abuzar.*
