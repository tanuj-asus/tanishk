import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create students table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE
        )''')
        
        # Create attendance table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )''')
        self.connection.commit()

    def add_student(self, name, age, email):
        self.cursor.execute('''INSERT INTO students (name, age, email) VALUES (?, ?, ?)''', (name, age, email))
        self.connection.commit()

    def get_student(self, student_id):
        self.cursor.execute('''SELECT * FROM students WHERE id = ?''', (student_id,))
        return self.cursor.fetchone()

    def update_student(self, student_id, name, age, email):
        self.cursor.execute('''UPDATE students SET name = ?, age = ?, email = ? WHERE id = ?''', (name, age, email, student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        self.cursor.execute('''DELETE FROM students WHERE id = ?''', (student_id,))
        self.connection.commit()

    def add_attendance(self, student_id, date, status):
        self.cursor.execute('''INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)''', (student_id, date, status))
        self.connection.commit()

    def get_attendance(self, student_id):
        self.cursor.execute('''SELECT * FROM attendance WHERE student_id = ?''', (student_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()