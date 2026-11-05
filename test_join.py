import duckdb

con = duckdb.connect("olist.duckdb")

result = con.sql("""
    SELECT c.customer_city, COUNT(*) AS total_orders
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_city
    ORDER BY total_orders DESC
    LIMIT 5
""")
print(result)