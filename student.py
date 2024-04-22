from dbgetter import DbGetter

class Student(DbGetter):
    
    table = "students"
    table_row_1 = "id"
    table_row_2 = "name"
    table_row_3 = "observation"

    def __init__(self, id, name, observation):
        self.id = id
        self.name = name
        self.observation = observation
    
    @classmethod
    def is_there_student(cls, id:int) -> bool:
        if(Student.connection.read("*", Student.table, f"WHERE id = {id}").fetchone()):
            return True
        return False

    @classmethod
    def get_student(cls, id: int) -> "Student":
        if Student.is_there_student(id):
            info = Student.connection.read("*", Student.table, f"WHERE id = {id}").fetchone()
            return Student(info[0], info[1], info[2])
        return
    
    @classmethod
    def save_student(cls, student: "Student") -> None:
        if Student.is_there_student(student.id) == False:
            insert_query = vars(student)
            Student.connection.insert(Student.table, insert_query)
        return

    @classmethod
    def update_student(cls, student: "Student") -> None:
        update_query = f"({Student.table_row_2}, {Student.table_row_3}) = ('{student.name}', '{student.info}')"
        Student.connection.update(update_query, Student.table, f" WHERE {Student.table_row_1} = {student.id}")
        return

    @classmethod
    def delete_student(cls, student: "Student") -> None:
        delete_query = f"{Student.table_row_1} = {student.id}"
        Student.connection.delete(Student.table, delete_query)
        return

if __name__ == "__main__":
    s1 = Student(12314, "João", "Inteligente e legal")
    Student.save_student(s1)
    sS1 = Student.is_there_student(12314)
    print(sS1)
    Student.delete_student(s1)
    sS1 = Student.is_there_student(12314)
    print(sS1)
    pass