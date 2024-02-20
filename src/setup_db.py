import sqlite3

def describe_database(c):
    result = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    tables = sorted(result)
    for (table_name, ) in tables:
        result = c.execute("PRAGMA table_info('%s')" % table_name).fetchall()
        print('Table:', table_name)
        for col in result:
            print('  ', col)


conn = sqlite3.connect("txs.db")
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS transactions""")
# FILL ME IN WITH YOUR TABLE SCHEMA
c.execute("""
CREATE TABLE IF NOT EXISTS transactions (
  tx_hash BLOB PRIMARY KEY,
  block_number INTEGER,  
  tx_data BLOB,
  sender BLOB,
  receiver BLOB
)
""")

describe_database(c)

c.close()
conn.close()
