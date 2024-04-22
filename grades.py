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
        self.course_id = grade
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
        insert_query = {cls.table_row_2: grade.course_id, cls.table_row_3: ClassType(grade.grade_type).value, cls.table_row_4: grade.info, cls.table_row_5: grade.date.strftime("%Y-%m-%d")}
        Class.connection.insert(Class.table, insert_query)
        return

    #TO DO down below
    @classmethod
    def update_class(cls, a_class: "Class") -> None:
        date = a_class.date.strftime("%Y-%m-%d")
        update_query = f"({Class.table_row_2}, {Class.table_row_3}, {Class.table_row_4}, {Class.table_row_5}, {Class.table_row_6}, {Class.table_row_7}) = ({a_class.course_id}, {ClassType(a_class.class_type).value}, '{date}', '{a_class.subject}', '{a_class.observation}', {a_class.was_held})"
        Class.connection.update(update_query, Class.table, f" WHERE {Class.table_row_1} = {a_class.id}")
    @classmethod
    def delete_class(cls, a_class: "Class") -> None:
        delete_query = f"{Class.table_row_1} = {a_class.id}"
        Class.connection.delete(Class.table, delete_query)
        return
    
    @classmethod
    def get_all_instances(cls) -> list["Class"]:
        list_of_classes = []
        info = Class.connection.read("*", Class.table).fetchall()
        for a_class in info:
            list_of_classes.append(Class(a_class[1], ClassType(int(a_class[2])), date.fromisoformat(a_class[3]), a_class[4], a_class[5], a_class[6], a_class[0]))
        return list_of_classes

    def __str__(self):
        if self.was_held:
            held_str = "Held"
        elif self.was_held == False:
            held_str = "Not held"
        d = self.date.strftime("%d %B, %Y")
        return f"Class Id:{self.id}, Course Id:{self.course_id}, Type:{ClassType(self.class_type).value}, Date: {d}, Subject: {self.subject}, Observation: {self.observation}, Status: {self.was_held}"

if __name__ == "__main__":
    pass