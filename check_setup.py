import os
import duckdb
from dotenv import load_dotenv

# 1. Database check
con = duckdb.connect("olist.duckdb")
tables = con.sql("SHOW TABLES").fetchall()
print("Database tables:", len(tables))
orders = con.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
print("Orders in database:", orders)
con.close()

# 2. Key check (sirf True/False dikhayenge, key nahi)
load_dotenv()
key = os.getenv("GEMINI_API_KEY")
print("Gemini key found:", key is not None and len(key) > 0)

# 3. Gemini library check
from google import genai
print("google-genai library: OK")