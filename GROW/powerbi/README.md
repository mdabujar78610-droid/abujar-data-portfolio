# GROW — Power BI Dashboard Build Guide

This folder contains DAX measures and dashboard specifications. The interactive Power BI Desktop file (.pbix) is not included yet; create it in Power BI Desktop using the steps below.

## 1. Load the dataset
1. Open Power BI Desktop.
2. Select **Get data → Text/CSV**.
3. Load `../dataset/samplesuperstore.csv`.
4. Confirm data types: Order Date and Ship Date = Date; Sales, Profit, Discount = Decimal Number; Quantity = Whole Number.
5. Rename the imported table to `Orders` if needed.

## 2. Add DAX measures
Open `GROW_DAX_Measures.dax` and create the measures in the model. If your imported column names differ, adjust the expressions.

## 3. Dashboard layout
- KPI cards: Total Sales, Total Profit, Profit Margin, Orders, Customers, Loss-Making Rows.
- Line chart: monthly Sales and Profit; use Order Date hierarchy or a proper Date table.
- Bar chart: Sales by Category.
- Bar chart: Profit by Region.
- Bar chart: Profit by Sub-Category, sorted ascending to surface weakest performers.
- Slicers: Order Date, Region, Category, Segment.

## 4. Validation checks
- Compare totals with the Excel workbook and Python output.
- Check that distinct order and customer counts use the intended IDs.
- Test slicers and cross-filtering.
- Confirm currency and date range before publishing.
- Treat negative-profit rows as investigation signals, not automatic data errors.
- A relationship between discount and profit is descriptive; it does not prove causation.

## 5. Save and publish
Save the finished report as `GROW_Dashboard.pbix` in this folder. Add a screenshot only after the actual report has been built and checked.

## Current status
DAX measures and a static dashboard preview are available. This guide is a build specification, not evidence that an interactive PBIX dashboard has already been implemented.
