import sqlite3

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def firstRun(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR,
                        info TEXT);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR,
                        teacher_id INTEGER,
                        created_at TIMESTAMP, 
                        times TEXT,
                        info TEXT);''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        observation TEXT);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses_students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        course_id INTEGER);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
                        course_id INTEGER,
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        type VARCHAR,
                        name VARCHAR,
                        date TIMESTAMP,
                        info TEXT,
                        observation TEXT,
                        wasTaken BOOL);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        course_id INTEGER,
                        info VARCHAR,
                        date TIMESTAMP);''')
 
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        test_id INTEGER,
                        grade FLOAT,
                        extra_point FLOAT,
                        observation TEXT);''')

        self.connection.commit()
    
    def insert(self, table: str, data: dict[str]):
        he = []
        va = []
        if data != {}:
            for h in data.keys():
                he.append(h)
            for v in data.values():
                va.append(v)
            headers = ""
            values = ""

            for item in he:
                headers += f"{item}, "

            for item in va:
                if type(item) == int:
                    values += f"{item}, "
                else:
                    values += f"\'{item}\', "

            query = f"INSERT INTO {table} ({headers[:-2]}) VALUES ({values[:-2]})"
            
            try:
                self.connection.execute(query)
                self.connection.commit()
            except sqlite3.IntegrityError as e:
                log().critical('Insert Error')

    def update(self, columns_and_values: str, table: str, condition: str = "" ):
        try:
            self.cursor.execute(f"UPDATE {table} set {columns_and_values} {condition}")
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            log().critical('Update Error')

    def read(self, arg: str, table: str, condition: str = "")-> list[tuple[str]]:
        try:
            result = self.cursor.execute(f"SELECT {arg} FROM {table} {condition}")
        except sqlite3.IntegrityError as e:
            log().critical('Read Error')
        return result
    
    def delete(self, table: str, condition: str):
        if table and condition != "":
            query = f"DELETE FROM {table} WHERE {condition}"
            
            try:
                self.cursor.execute(query)
                self.connection.commit()
            except sqlite3.IntegrityError as e:
                log().critical('Delete Error')

    def closeConnection(self):
        self.connection.close()

        
if __name__ == "__main__":
    db = Database()
    db.firstRun()
    db.insert("teachers", {'id': 0, 'name': 'jozephf', 'info': 'whatever'})
    # print(db.read('*', "teacher").fetchall())
    db.insert("teachers", {'id': 1, 'name': 'joao', 'info': 'casdaseda'})
    print(db.read('*', "teachers").fetchall())
    # db.delete("teacher", "id = 0")
    # print(db.read('*', "teacher"))
    # db.delete("teacher", "id = 1")
    # print(db.read('*', "teacher"))
    
    # print(db.read('*', "teacher").fetchall())