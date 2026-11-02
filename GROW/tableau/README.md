# GROW Tableau Dashboard

The GROW project uses Tableau as its primary dashboard and visualization tool.

## Workbook contents
- 1 dashboard
- 12 worksheets: five KPI views, monthly sales/profit trend, category sales, regional profit, sub-category profit, and three highlight views
- 3 interactive highlight actions
- Calculated fields for Profit Margin, distinct Orders, and Negative Profit count

## Dataset connection
The prepared workbook uses a relative `dataset` folder. Place `GROW_Tableau_Dashboard.twb` in the GROW project root, beside `dataset/samplesuperstore.csv`. If Tableau prompts for the source, select that CSV.

## Validation before publishing
The workbook's Sales and Profit formats currently use ₹, while the written sample KPI summary uses $. Confirm the intended currency and make the dashboard and project documentation consistent.

The old static SVG chart gallery has been removed. The actual Tableau workbook is prepared locally but still needs to be uploaded to GitHub by the repository owner.
