import sqlite3
DATABASE = 'questions.db'
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        profession TEXT NOT NULL,
        skill TEXT NOT NULL,
        question TEXT NOT NULL
    );
    """)

    sample_data = [
        ('Fresher', 'python', 'What is your experience with Python?'),
        ('Fresher', 'python', 'Explain how Python handles memory management.'),
        ('Experienced', 'python', 'How do you optimize Python performance?'),
        ('Experienced', 'python', 'What are the key differences between Python 2 and Python 3?'),
    ]

    cursor.executemany("""
    INSERT INTO questions (profession, skill, question)
    VALUES (?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized and populated with sample data.")
