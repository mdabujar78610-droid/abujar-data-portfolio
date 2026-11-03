# GROW Tableau Dashboard

This folder contains the editable Tableau workbook for the GROW retail analytics case study.

## Workbook contents
- 1 dashboard
- 12 worksheets
- KPI views for sales, profit, margin, orders, and customers
- Category, regional, sub-category, and monthly trend analysis
- Interactive highlight actions
- Calculated fields for profit margin, distinct orders, and negative-profit count

## Open the workbook
1. Download `GROW_Tableau_Dashboard.twb` from this folder.
2. Keep the project dataset at `GROW/dataset/samplesuperstore.csv`.
3. Open the workbook in Tableau Desktop.
4. If Tableau asks for the data source, reconnect it to `GROW/dataset/samplesuperstore.csv`.
5. Refresh the data and confirm that all worksheets and the dashboard render without errors.

## Currency and metric consistency
The project README reports Sales and Profit in USD ($). Keep the Tableau number formats and KPI values consistent with that reporting convention. Check the workbook's data-source locale/currency defaults as well as worksheet-level number formatting; changing only a displayed label may not update the underlying defaults.

## Files
- [Editable Tableau workbook](GROW_Tableau_Dashboard.twb)
- [Dashboard preview](../dashboard/grow_dashboard.png)
- [Chart gallery](../charts/)

The PNG files are static previews. Use the TWB workbook for the editable Tableau analysis.
