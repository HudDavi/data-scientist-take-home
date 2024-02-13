import sqlite3

conn = sqlite3.connect("txs.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS transactions (
  id INTEGER PRIMARY KEY,
  data BLOB 
)
""")

