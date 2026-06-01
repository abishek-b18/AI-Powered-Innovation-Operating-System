import sqlite3

DATABASE = "foundryai.db"

def connect_db():
    return sqlite3.connect(DATABASE)


def create_tables():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ideas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        startup_name TEXT,
        industry TEXT,
        target_market TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_idea(startup_name, industry, target_market, description):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO ideas(
        startup_name,
        industry,
        target_market,
        description
    )
    VALUES(?,?,?,?)
    """,
    (
        startup_name,
        industry,
        target_market,
        description
    ))

    conn.commit()
    conn.close()