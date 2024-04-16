from db_getter import Db_getter

class Course(Db_getter):

    def __init__(self, connection) -> None:
        super().__init__(connection)
        self.schedule =[]
        self.classes = []
        self.extraClasses = []
        self.summary = []
        self.subjects = []
        self.grades = []
        self.table = "course"
        self.id = -1
    
    def get_information(self, id: int):
        info = self.connection.read("*", self.table, f"WHERE id = {id}").fetchone()

        pass
        

if __name__ == "__main__":
    from database import Database
    db = Database()
    c1 = Course(db, 0)
