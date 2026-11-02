# GROW — Retail Sales & Profitability Analysis

**Junior Data Analyst portfolio project | Excel • SQL • Python • Tableau**

## Project overview
GROW is a simulated retail analytics case study built with the Sample Superstore dataset. The project examines sales, profit, category and regional performance, sub-category profitability, discount patterns, and data quality.

> **Dataset note:** This is sample data, not verified data from a real GROW company. The source dates run from 3 Jan 2023 through 30 Dec 2026. Treat the findings as analysis of a supplied sample dataset, not as verified company history.

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

These are descriptive results from the sample file, not causal conclusions or claims about an actual company. Confirm currency formatting before presenting the Tableau views alongside these dollar-denominated sample KPIs.

## Tools and analysis
- **Excel:** KPI summary, data checks, and analysis tables.
- **SQL:** reusable queries for sales, profit, category, region, and sub-category analysis.
- **Python:** Pandas data-quality checks, KPI calculations, and category/region summaries.
- **Tableau:** the main dashboard workbook, with 12 worksheets and 3 interactive highlight actions.

## Tableau dashboard
The supplied Tableau workbook contains one dashboard and 12 worksheets. The worksheets cover:

| Dashboard component | Worksheet |
|---|---|
| Total Profit KPI | KPI - Total Profit |
| Total Sales KPI | KPI - Total Sales |
| Profit Margin KPI | KPI - Profit Margin |
| Orders KPI | KPI - Orders |
| Negative Profit KPI | KPI - Negative Profit |
| Monthly trend | Monthly Sales and Profit Trend |
| Category analysis | Sales by Category |
| Regional analysis | Profit by Region |
| Sub-category analysis | Profit by Sub-Category |
| Interactive highlight views | Sub-Category Highlight A, Sub-Category Highlight B, Regional Profit Highlight |

The workbook also contains **3 interactive highlight actions**. The calculated fields include:
- Profit Margin: `SUM([Profit]) / SUM([Sales])`
- Orders: `COUNTD([Order ID])`
- Negative Profit count: `SUM(IF [Profit] < 0 THEN 1 ELSE 0 END)`

### Data connection
The uploaded workbook is stored at [`tableau/GROW_Tableau_Dashboard.twb`](tableau/GROW_Tableau_Dashboard.twb). Its relative data connection points to `../dataset/samplesuperstore.csv`. Keep the existing `dataset` folder in place. If Tableau asks for the source, select `GROW/dataset/samplesuperstore.csv`.

### Currency validation
The Tableau workbook formats Sales and Profit with a rupee symbol (₹), while the sample KPI calculations above are written in US dollars ($). Confirm the intended currency and make the displays consistent before publishing or using dashboard screenshots.

### Workbook availability
The renamed Tableau workbook is now uploaded to this repository: [`GROW_Tableau_Dashboard.twb`](tableau/GROW_Tableau_Dashboard.twb). Open it with Tableau Desktop to explore the interactive dashboard and worksheets.

## Run the Python analysis
From the repository root:

```bash
pip install pandas
python GROW/grow_analysis.py GROW/dataset/samplesuperstore.csv
```

The script prints data-quality checks, KPIs, category performance, and regional performance. Tableau is the project's dashboard and visualization tool; the previous standalone SVG chart gallery has been removed.
