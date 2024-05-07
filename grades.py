from dbgetter import DbGetter
from datetime import date, datetime
from gradetype import GradeType

class Grade(DbGetter):

    table = "grades"  
    columns = [
        "id", 
        "course_id", 
        "grade_type", 
        "infomation", 
        "date"
        ]
    instantiation_attr_order = [1, 2, 3, 4, 0] #compared with  columns list above because some attr have default values
    instantiation_attr_types = [int, GradeType, str, datetime, int] #in the order of the list instaciation_attr_order

    
    def __init__(self, course_id: int, grade_type: GradeType, information: str, date: datetime,  id: int = -1) -> None:
        self.id: int = id
        self.course_id: int  = course_id
        self.grade_type = grade_type
        self.information = information
        self.date: datetime = date
    
    def __str__(self):
        d = self.date.strftime("%d %B, %Y")
        return f"Grade Id:{self.id}, Course Id:{self.course_id}, Type:{GradeType(self.grade_type).value}, Information: {self.information}, Date: {d}"

if __name__ == "__main__":
    # g1 = Grade(1, GradeType.EXAM, "1ª Avaliação Escrita", date.fromisoformat("2024-05-15"))
    # g1.save_instance(g1)
    # g1 = Grade.get_instance(5)
    # g1.date = date.fromisoformat("2024-07-10")
    # Grade.update_instance(g1)
    # Grade.delete_by_id(-1)
    # g1 = Grade.get_instance(4)
    # print(g1)
    # Grade.delete_grade(g1)
    # g10 = Grade(2, GradeType.EXAM, date.fromisoformat("2014-09-09"), "Segundo teste")
    # Grade.save_instance(g10)
    # Grade.delete_by_id(6)
    for each in Grade.get_all():
        print(each)