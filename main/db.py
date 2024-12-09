import sqlite3

# Connect to the database
conn = sqlite3.connect("clients.db")
cursor = conn.cursor()

# Create the clients table
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    student_id TEXT NOT NULL,
    login_name TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
