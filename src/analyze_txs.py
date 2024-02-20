import sqlite3

conn = sqlite3.connect("txs.db")
c = conn.cursor()

results = c.execute("SELECT * FROM transactions LIMIT 10").fetchall()
print(results)

c.close()
conn.close()