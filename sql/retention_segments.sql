-- SQLite. Run after notebook 01 loads the prepared data into customers.
-- Grain: one customer per row. Churn = 1 for attrited, 0 for existing.
-- These segments overlap; do not add their counts or churn shares together.
WITH segment_rows AS (
    SELECT '01. All customers' AS segment, Churn FROM customers
    UNION ALL
    SELECT '02. Utilization below 25%', Churn FROM customers
    WHERE Avg_Utilization_Ratio < 0.25
    UNION ALL
    SELECT '03. Two products', Churn FROM customers
    WHERE Total_Relationship_Count = 2
    UNION ALL
    SELECT '04. Six products', Churn FROM customers
    WHERE Total_Relationship_Count = 6
    UNION ALL
    SELECT '05. Five contacts in 12 months', Churn FROM customers
    WHERE Contacts_Count_12_mon = 5
    UNION ALL
    SELECT '06. Six contacts in 12 months', Churn FROM customers
    WHERE Contacts_Count_12_mon = 6
    UNION ALL
    SELECT '07. Blue cardholders', Churn FROM customers
    WHERE Card_Category = 'Blue'
    UNION ALL
    SELECT '08. Platinum cardholders', Churn FROM customers
    WHERE Card_Category = 'Platinum'
),
overall AS (
    SELECT SUM(Churn) AS all_churned_customers FROM customers
)
SELECT
    segment,
    COUNT(*) AS customers,
    SUM(Churn) AS churned_customers,
    ROUND(100.0 * SUM(Churn) / COUNT(*), 2) AS churn_rate_pct,
    ROUND(
        100.0 * SUM(Churn) / NULLIF((SELECT all_churned_customers FROM overall), 0),
        2
    ) AS share_of_all_churn_pct
FROM segment_rows
GROUP BY segment
ORDER BY segment;
