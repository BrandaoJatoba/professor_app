import sqlite3

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('DB\database.db')
        self.cursor = self.connection.cursor()

    def firstRun(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                        id INTEGER PRIMARY KEY,
                        name VARCHAR,
                        info TEXT);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title VARCHAR,
                        teacher_id INTEGER,
                        schedule TEXT,
                        info TEXT,
                        total_credit_hours FLOAT,
                        finished INTEGER);''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        observation TEXT);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses_students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        course_id INTEGER);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        course_id INTEGER,
                        class_type INTERGER,
                        date DATE,
                        subject TEXT,
                        observation TEXT,
                        credit_hours FLOAT,
                        was_held INTEGER);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        course_id INTEGER,
                        grade_type INT,
                        information VARCHAR,
                        date DATE);''')
 
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students_grades (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        grade_id INTEGER,
                        grade FLOAT,
                        extra_point FLOAT,
                        observation TEXT);''')

        self.connection.commit()
    
    def insert(self, table: str, data: dict[str]) -> None:
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

    def update(self, columns_and_values: str, table: str, condition: str = "" ) -> None:
        try:
            self.cursor.execute(f"UPDATE {table} SET {columns_and_values} {condition};")
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            log().critical('Update Error')

    def read(self, arg: str, table: str, condition: str = "") -> list[tuple[str]]:
        try:
            result = self.cursor.execute(f"SELECT {arg} FROM {table} {condition}")
        except sqlite3.IntegrityError as e:
            log().critical('Read Error')
        return result
    
    def delete(self, table: str, condition: str) -> None:
        if table and condition != "":
            query = f"DELETE FROM {table} WHERE {condition}"
            
            try:
                self.cursor.execute(query)
                self.connection.commit()
            except sqlite3.IntegrityError as e:
                log().critical('Delete Error')

    def closeConnection(self) -> None:
        self.connection.close()

        
if __name__ == "__main__":
    db = Database()
    # db.firstRun()
    # db.insert("teachers", {'id': 0, 'name': 'jozephf', 'info': 'whatever'})
    # db.insert("teachers", {'id': 1, 'name': 'joao', 'info': 'casdaseda'})
    print(db.read('*', "teachers").fetchall())
    # print(db.read('*', "teacher").fetchall())
    # db.delete("teacher", "id = 0")
    # print(db.read('*', "teacher"))
    # db.delete("teacher", "id = 1")
    # print(db.read('*', "teacher"))
    