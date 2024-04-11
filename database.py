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
                values += f"\'{item}\', "

            query = f"INSERT INTO {table} ({headers[:-2]}) VALUES ({values[:-2]})"
            print(query)
            try:
                self.connection.execute(query)
                self.connection.commit()
            except sqlite3.IntegrityError as e:
                log().critical('Generic Error')

    def read(self, arg: str, table: str, condition: str = "")-> list[tuple[str]]:

        result = self.cursor.execute(f"SELECT {arg} FROM {table} {condition}")
        return result
    
    def delete(self, table: str, condition: str):
        if table and condition != "":
            query = f"DELETE FROM {table} WHERE {condition}"
            
            try:
                self.cursor.execute(query)
                self.connection.commit()
            except sqlite3.IntegrityError as e:
                log().critical('Generic Error')

    def closeConnection(self):
        self.connection.close()

        
if __name__ == "__main__":
    db = Database()
    #db.firstRun()
    # db.insert("teacher", {'id': 0, 'name': 'jozephf', 'info': 'whatever'})
    # print(db.read('*', "teacher").fetchall())
    # db.insert("teacher", {'id': 1, 'name': 'joao', 'info': 'casdaseda'})
    # print(db.read('*', "teacher").fetchall())
    # db.delete("teacher", "id = 0")
    # print(db.read('*', "teacher"))
    # db.delete("teacher", "id = 1")
    # print(db.read('*', "teacher"))
    
    # print(db.read('*', "teacher").fetchall())