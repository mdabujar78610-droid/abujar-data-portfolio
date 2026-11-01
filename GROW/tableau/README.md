# GROW Tableau Dashboard

This folder is reserved for the Tableau workbook submitted for the GROW retail analytics project.

## Workbook review

- 1 dashboard and 12 worksheets
- KPI calculations: Profit Margin = SUM(Profit) / SUM(Sales); distinct Orders = COUNTD(Order ID); Negative Profit = count of rows where Profit is below zero
- Dashboard views include monthly Sales and Profit, Sales by Category, Profit by Region, and Profit by Sub-Category
- Three generated highlight actions are present

## Data connection

The submitted Tableau workbook references a local Windows file path. The source dataset is maintained in `../dataset/samplesuperstore.csv`. If Tableau reports a missing file, use **Data > [data source] > Edit Connection** and select that CSV.

## Important validation before publishing

The workbook formats Sales and Profit with a rupee symbol (₹), while the project's written sample-data KPI summary uses dollars ($). Confirm the intended currency and make the workbook, charts, and README consistent. Also note that a `.twb` file does not embed the CSV; keep the dataset alongside the workbook or package the workbook as `.twbx`.

The workbook file itself must be placed in this folder as `GROW_Tableau_Dashboard.twb` after the source connection is checked.