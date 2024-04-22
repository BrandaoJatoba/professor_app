from dbgetter import DbGetter
from datetime import date
from gradetype import GradeType

class Grade(DbGetter):

    table = "grades"    
    table_row_1 = "id"
    table_row_2 = "course_id"
    table_row_3 = "type"
    table_row_4 = "info"
    table_row_5 = "date"

    
    def __init__(self, course_id: int, grade_type: GradeType, date: date, information: str,  id: int = -1) -> None:
        self.course_id = course_id
        self.grade_type = grade_type
        self.information = information
        self.date = date
        self.id = id
    
    @classmethod
    def get_intance(cls, id: int) -> "Grade":
        if cls.is_there_instance(id):
            info = cls.connection.read("*", cls.table, f"WHERE id = {id}").fetchone()
            return Grade(info[1], GradeType(int(info[2])), date.fromisoformat(info[4]), info[3], info[0])
        return

    @classmethod
    def save_grade(cls, grade: "Grade") -> None:
        insert_query = {cls.table_row_2: grade.course_id, cls.table_row_3: GradeType(grade.grade_type).value, cls.table_row_4: grade.information, cls.table_row_5: grade.date.strftime("%Y-%m-%d")}
        Grade.connection.insert(cls.table, insert_query)
        return

    #TO DO down below
    @classmethod
    def update_grade(cls, grade: "Grade") -> None:
        date = grade.date.strftime("%Y-%m-%d")
        update_query = f"({cls.table_row_2}, {cls.table_row_3}, {cls.table_row_4}, {cls.table_row_5}) = ({grade.course_id}, {GradeType(grade.grade_type).value}, '{grade.information}', '{date}')"
        Grade.connection.update(update_query, cls.table, f" WHERE {cls.table_row_1} = {grade.id}")
    @classmethod
    def delete_grade(cls, grade: "Grade") -> None:
        delete_query = f"{cls.table_row_1} = {grade.id}"
        Grade.connection.delete(cls.table, delete_query)
        return
    
    @classmethod
    def get_all_instances(cls) -> list["Grade"]:
        list_of_grades = []
        info = Grade.connection.read("*", cls.table).fetchall()
        for grade in info:
            list_of_grades.append(Grade(grade[1], GradeType(int(grade[2])), date.fromisoformat(grade[4]), grade[3], grade[0]))
        return list_of_grades

    def __str__(self):
        d = self.date.strftime("%d %B, %Y")
        return f"Grade Id:{self.id}, Course Id:{self.course_id}, Type:{GradeType(self.grade_type).value}, Information: {self.information}, Date: {d}"

if __name__ == "__main__":
    # g1 = Grade(1, GradeType.EXAM, date.fromisoformat("2024-07-11"), "2ª Avaliação Escrita" )
    # g1.save_grade(g1)
    # g1 = Grade.get_intance(3)
    # g1.date = date.fromisoformat("2024-07-10")
    # Grade.update_grade(g1)
    # Grade.delete_by_id(3)
    # g1 = Grade.get_intance(2)
    # Grade.delete_grade(g1)
    for each in Grade.get_all_instances():
        print(each) 