import duckdb

result = duckdb.sql("DESCRIBE SELECT * FROM 'data/olist_orders_dataset.csv'")
print(result)