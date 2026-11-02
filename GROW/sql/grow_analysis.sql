-- GROW Retail Analytics (SQLite-compatible)
-- Load the CSV into a table named superstore.
-- Do not treat repeated Order ID values as duplicates: one order can contain multiple product rows.

-- 1. Overall KPIs
SELECT
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit,
  ROUND(100.0 * SUM(Profit) / NULLIF(SUM(Sales), 0), 2) AS profit_margin_pct,
  COUNT(DISTINCT "Order ID") AS unique_orders,
  COUNT(DISTINCT "Customer ID") AS unique_customers
FROM superstore;

-- 2. Sales and profit by category
SELECT Category, ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit,
       ROUND(100.0*SUM(Profit)/NULLIF(SUM(Sales),0),2) AS margin_pct
FROM superstore
GROUP BY Category ORDER BY sales DESC;

-- 3. Profit by region
SELECT Region, ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit
FROM superstore
GROUP BY Region ORDER BY profit DESC;

-- 4. Lowest-profit subcategories to investigate
SELECT "Sub-Category", ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit
FROM superstore
GROUP BY "Sub-Category"
ORDER BY profit ASC LIMIT 10;

-- 5. Discount level vs profit (descriptive, not causal)
SELECT Discount, COUNT(*) AS line_items,
       ROUND(SUM(Sales),2) AS sales,
       ROUND(SUM(Profit),2) AS profit,
       ROUND(100.0*SUM(Profit)/NULLIF(SUM(Sales),0),2) AS margin_pct
FROM superstore
GROUP BY Discount ORDER BY Discount;

-- 6. Monthly trend. Requires parseable Order Date values.
SELECT strftime('%Y-%m', date("Order Date")) AS order_month,
       ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
FROM superstore
GROUP BY strftime('%Y-%m', date("Order Date"))
ORDER BY order_month;

-- 7. Data-quality checks
SELECT COUNT(*) AS rows, COUNT(DISTINCT "Row ID") AS unique_row_ids FROM superstore;
SELECT COUNT(*) AS exact_duplicate_candidates
FROM (
  SELECT "Row ID", "Order ID", "Order Date", "Ship Date", "Product ID", Sales, Profit, COUNT(*) AS n
  FROM superstore
  GROUP BY "Row ID", "Order ID", "Order Date", "Ship Date", "Product ID", Sales, Profit
  HAVING COUNT(*) > 1
);
