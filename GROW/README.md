# GROW — Retail Sales & Profitability Analysis

**Junior Data Analyst portfolio project | Excel • SQL • Python • Tableau**

## Project overview
GROW is a simulated retail analytics case study built with the Sample Superstore dataset. It examines sales, profit, category and regional performance, sub-category profitability, discount patterns, and data quality.

> **Dataset note:** This is sample data, not verified data from a real GROW company. The source dates run from 3 Jan 2023 through 30 Dec 2026. Treat findings as analysis of the supplied sample dataset, not verified company history.

## Dataset and quality checks
- 10,194 transaction rows and 21 columns
- 5,111 distinct orders and 804 distinct customers
- The supplied checks found no missing cells, exact duplicate rows, duplicate Row IDs, or ship-before-order records.

## Key results from the sample data
- **Total sales:** $2,326,534.35
- **Total profit:** $292,296.81
- **Profit margin:** 12.56%
- **Unique orders:** 5,111
- **Unique customers:** 804
- **Negative-profit line items:** 1,901 (18.65%)
- **Highest category sales:** Technology — $839,893.28
- **Lowest sub-category profit:** Tables — -$17,753.21
- **Lowest regional profit:** Central — $39,865.31

These are descriptive results from the supplied sample file, not causal conclusions or claims about an actual company.

## Tools and analysis
- **Excel:** KPI summary, data-quality audit, category/region/monthly analysis, and analysis data table.
- **SQL:** reusable queries for overall KPIs, category, region, sub-category, discount, monthly trends, and data-quality checks (included in the project ZIP).
- **Python:** Pandas data-quality checks, KPI calculations, category/region summaries, and repeatable analysis.
- **Tableau:** primary interactive dashboard workbook with 12 worksheets and 3 highlight actions.
- **Power BI:** DAX measures and dashboard layout notes are included in the ZIP; a finished `.pbix` report is not currently in the repository.

## Tableau dashboard
The workbook is stored at [GROW_Tableau_Dashboard.twb](tableau/GROW_Tableau_Dashboard.twb). It contains one dashboard and 12 worksheets: five KPI views, monthly sales/profit trend, category sales, regional profit, sub-category profit, and three highlight views. It also contains 3 interactive highlight actions.

### Dataset connection
The workbook's relative data connection points to `../dataset/samplesuperstore.csv`. Keep the existing `GROW/dataset` folder in place. If Tableau asks for the source, select `GROW/dataset/samplesuperstore.csv`.

### Currency and date validation
The written KPI values above are expressed in US dollars to match the source project report. Before publishing screenshots, verify that Tableau's number formatting uses the intended currency. Also disclose the dataset's unusual 2023–2026 date range.

## Main project files
- `GROW_Analytics_Workbook.xlsx` — Excel analysis workbook
- `GROW_Resume_Project_Pack.zip` — source pack containing SQL, Python, Excel, reports, sample CSV, and Power BI DAX notes
- `dataset/samplesuperstore.csv` — source sample data
- `tableau/GROW_Tableau_Dashboard.twb` — Tableau workbook
- `grow_analysis.py` — reproducible Python analysis script

## Run the Python analysis
From the repository root:
```bash
pip install pandas
python GROW/grow_analysis.py GROW/dataset/samplesuperstore.csv
```

## Limitations and next steps
- The sample data is not verified real-company data.
- Discount/profit association is descriptive and does not establish causation.
- The ZIP contains an older report titled SmartMart; use the GROW report for this renamed project.
- A finished Power BI `.pbix` file and verified dashboard screenshots are not currently present.