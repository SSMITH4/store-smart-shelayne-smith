-- File: 10_create_customers.sql
-- Compatible with SQLite, DuckDB, dbt (DuckDB), and SQLMesh
-- DATE Field Note:
-- - SQLite: Uses TEXT for date fields (store as 'YYYY-MM-DD' ISO format)
-- - DuckDB and others: Support native DATE type (can parse ISO-formatted TEXT)
-- - CSV Columns: CustomerID,Name,Region,JoinDate

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    Name TEXT,
    Region TEXT,
    JoinDate TEXT,  -- use ISO format: 'YYYY-MM-DD'
    LoyaltyPoints INTEGER,
    age INTEGER
);