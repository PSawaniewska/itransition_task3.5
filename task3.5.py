import json
import re
import sqlite3

with open("task3.5_files/task1_d.json", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r':(\w+)=>', r'"\1":', text)
data = json.loads(text)

conn = sqlite3.connect("books.db")
conn.execute("DROP TABLE IF EXISTS books")
conn.execute("""
    CREATE TABLE books (
        id TEXT, title TEXT, author TEXT, genre TEXT,
        publisher TEXT, year INTEGER, price TEXT
    )
""")

rows = [(str(b["id"]), b["title"], b["author"], b["genre"],
         b["publisher"], b["year"], b["price"]) for b in data]

conn.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)", rows)
conn.commit()

print(conn.execute("SELECT COUNT(*) FROM books").fetchone())


with open("summary.sql", encoding="utf-8") as f:
    conn.executescript(f.read())

for row in conn.execute("SELECT * FROM summary LIMIT 5"):
    print(row)

conn.close()