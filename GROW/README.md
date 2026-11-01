# GROW — Retail Sales & Profitability Analysis

**Junior Data Analyst portfolio project | Excel • SQL • Python • Power BI**

## Project overview
GROW is a simulated retail-business case study built with the supplied Sample Superstore dataset. It explores sales, profit, category and regional performance, sub-category profitability, discount patterns, and data quality.

> **Dataset note:** This is sample data, not verified data from a real GROW company. The source dates run from 3 Jan 2023 through 30 Dec 2026, which extends beyond 31 Oct 2026. Validate the date range before presenting it as historical performance.

## Dataset and quality checks
- 10,194 transaction rows and 21 columns
- 5,111 distinct orders and 804 distinct customers
- No missing cells, exact duplicate rows, duplicate Row IDs, or ship-before-order records detected by the supplied checks

## Key results from the supplied sample data
- **Total sales:** $2,326,534.35
- **Total profit:** $292,296.81
- **Profit margin:** 12.56%
- **Negative-profit line items:** 1,901 (18.65%)
- **Highest category sales:** Technology — $839,893.28
- **Lowest sub-category profit:** Tables — -$17,753.21
- **Lowest regional profit:** Central — $39,865.31

These are descriptive results from the sample file, not causal conclusions or claims about an actual company.

## Dashboard preview
![GROW dashboard preview](charts/GROW_Dashboard_Preview.svg)

## Visuals and project files
- `charts/GROW_Dashboard_Preview.svg` — static dashboard overview shown in this repository.
- The downloadable project pack contains the updated Excel workbook with a chart-gallery sheet, five exported chart images, the source sample dataset, Python analysis, SQL queries, Power BI DAX measures, and the supplied PDF reports.

The repository preview is a static visual. The full set of chart images and the Excel workbook are included in the downloadable project pack, not embedded as individual files in this GitHub folder.



## Individual chart visuals

The charts below are generated from the included sample dataset and are available as separate SVG files:

- [Sales by Category — Bar Chart](charts/01_sales_by_category_bar.svg)
- [Sales Mix by Category — Pie Chart](charts/02_sales_mix_pie.svg)
- [Monthly Sales & Profit — Line Chart](charts/03_monthly_sales_profit_line.svg)
- [Profit by Region — Bar Chart](charts/04_profit_by_region_bar.svg)
- [Profit by Sub-category — Bar Chart](charts/05_profit_by_subcategory_bar.svg)

## Power BI report plan
Import the `Analysis_Data` sheet into Power BI Desktop. Add KPI cards for sales, profit, margin, order count, and customer count; a monthly line chart; category sales and sub-category profit bar charts; and regional profit comparison. Add slicers for order date, region, category, segment, and ship mode. Use a proper Date table for time intelligence.


## Power BI implementation files
- [DAX measures and dashboard model setup](powerbi/GROW_DAX_Measures.dax)

The DAX file provides KPI measures and a recommended model layout. The interactive `.pbix` report itself has not yet been created or tested in Power BI Desktop.
