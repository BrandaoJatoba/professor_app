import sqlite3

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def firstRun(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teacher (
                        id interger,
                        name varchar,
                        info text);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS course (
                        id integer Primary key,
                        name varchar,
                        teacher_id integer,
                        created_at timestamp, 
                        times text,
                        info text);''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                        id interger,
                        name text,
                        course_id interger,
                        observation text);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS class (
                        course_id interger,
                        id interger,
                        type varchar,
                        name varchar,
                        date timestamp,
                        info text,
                        observation text,
                        wasTaken bool);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS test (
                        id integer,
                        course_id integer,
                        info varchar,
                        date timestamp);''')
 
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS grade (
                        student_id integer,
                        test_id integer,
                        grade float,
                        extra_point float,
                        observation text);''')
    
    def closeConnection(self):
        self.connection.close()

        
if __name__ == "__main__":
    db = Database()
    db.firstRun()