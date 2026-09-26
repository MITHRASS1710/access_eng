import sqlite3
import pandas as pd

DB_NAME = "complaints.db"

# ---------------- Database Initialization ----------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        description TEXT,
        anonymous TEXT,
        name TEXT,
        phone TEXT
    )
    """)

    # Ensure all columns exist (for existing tables)
    required_columns = ["category", "description", "anonymous", "name", "phone"]
    cursor.execute("PRAGMA table_info(complaints)")
    existing_columns = [col[1] for col in cursor.fetchall()]
    for col in required_columns:
        if col not in existing_columns:
            cursor.execute(f"ALTER TABLE complaints ADD COLUMN {col} TEXT")

    conn.commit()
    conn.close()

# Call initialization at import
init_db()


# ---------------- Insert Complaint ----------------
def insert_complaint(category, description, anonymous, name, phone):
    """
    Insert a new complaint into the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO complaints (category, description, anonymous, name, phone)
        VALUES (?, ?, ?, ?, ?)
    """, (category, description, anonymous, name, phone))
    conn.commit()
    conn.close()


# ---------------- Fetch Complaints ----------------
def get_all_complaints():
    """
    Fetch all complaints as a pandas DataFrame.
    """
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM complaints", conn)
    conn.close()
    return df