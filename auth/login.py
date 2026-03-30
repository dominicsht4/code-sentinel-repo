
# Intentional SQL injection vulnerability for testing
import sqlite3
DB_PASSWORD = "admin@12345"
def login(username, password):
    conn = sqlite3.connect("users.db")
    print(DB_PASSWORD)
    # VULNERABILITY: string concatenation in SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = conn.execute(query)
    return result.fetchone()
