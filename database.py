import sqlite3

DATABASE = "students.db"


def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            m1 INTEGER NOT NULL,
            m2 INTEGER NOT NULL,
            m3 INTEGER NOT NULL,
            total INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_result(name, m1, m2, m3, total, grade):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, m1, m2, m3, total, grade)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, m1, m2, m3, total, grade))

    conn.commit()
    conn.close()


def get_results():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    conn.close()
    return results


if __name__ == "__main__":
    create_table()
    print("Database and students table created successfully.")