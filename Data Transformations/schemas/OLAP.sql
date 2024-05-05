CREATE SCHEMA olap;

CREATE TABLE olap.sales_summary (
    region_id INT,
    total_sales DECIMAL(12, 2),
    average_order_amount DECIMAL(12, 2),
    total_orders INT
);

CREATE TABLE olap.customer_insights (
    customer_id INT,
    lifetime_value DECIMAL(12, 2),
    purchase_count INT
);
