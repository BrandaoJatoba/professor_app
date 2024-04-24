from dbgetter import DbGetter
from database import Database

class StudentsGrades(DbGetter):
    
    table = "students_grades"
    columns = ["id", "student_id", "grade_id", "grade,", "extra_point", "observation"]

    def __init__(self, student_id: int, grade_id: int, grade: float, extra_point: float, observation: str, id: int = -1):
        self.id: int = id
        self.student_id: int = student_id
        self.grade_id: int = grade_id
        self.grade: float = grade
        self.extra_point: float = extra_point
        self.observation: str = observation

if __name__ == "__main__":
    #db_connection = Database()
    #db_connection.cursor.execute("ALTER TABLE grades RENAME COLUMN info TO information;")
    ...