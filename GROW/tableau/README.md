# GROW Tableau Dashboard

The GROW project uses Tableau as its primary dashboard and visualization tool.

## Workbook contents
- 1 dashboard
- 12 worksheets: five KPI views, monthly sales/profit trend, category sales, regional profit, sub-category profit, and three highlight views
- 3 interactive highlight actions
- Calculated fields for Profit Margin, distinct Orders, and Negative Profit count

## Dataset connection
The workbook is uploaded here as [`GROW_Tableau_Dashboard.twb`](GROW_Tableau_Dashboard.twb). Its relative connection points to `../dataset/samplesuperstore.csv`, which is stored in the GROW project folder. If Tableau prompts for the source, select `GROW/dataset/samplesuperstore.csv`.

## Validation before publishing
The workbook's Sales and Profit formats currently use ₹, while the written sample KPI summary uses $. Confirm the intended currency and make the dashboard and project documentation consistent.

The old static SVG chart gallery has been removed. The actual Tableau workbook is committed in this folder and is available from the repository.
