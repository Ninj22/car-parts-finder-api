import sqlite3

# Connect to SQLite database (it creates the file if it doesn't exist)
conn = sqlite3.connect('parts.db')
cursor = conn.cursor()

# Create the `parts` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    part TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Insert sample data (optional step)
sample_data = [
    ("Toyota", "Corolla", 2022, "Brake Pads", 50),
    ("Honda", "Civic", 2021, "Air Filter", 20),
    ("Ford", "Focus", 2020, "Oil Filter", 15)
]

cursor.executemany('''
INSERT INTO parts (brand, model, year, part, price)
VALUES (?, ?, ?, ?, ?)
''', sample_data)

conn.commit()
conn.close()
