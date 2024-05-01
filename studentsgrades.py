from dbgetter import DbGetter
from database import Database

class StudentsGrades(DbGetter):
    
    table = "students_grades"
    columns =   [
                "id", 
                "student_id", 
                "grade_id", 
                "grade,", 
                "extra_point", 
                "observation"
                ]
    instantiation_attr_order = [1, 2, 3, 4, 5, 0]
    instantiation_attr_types = [int, int, float, float, str, int]

    def __init__(self, student_id: int, grade_id: int, grade: float, extra_point: float, observation: str, id: int = -1):
        self.id: int = id
        self.student_id: int = student_id
        self.grade_id: int = grade_id
        self.grade: float = grade
        self.extra_point: float = extra_point
        self.observation: str = observation

    def __str__(self):
        return f"Id: {self.id}, Student Id: {self.student_id}, Grade Id: {self.grade_id}, Grade: {self.grade}, Extra Point: {self.extra_point}, Observation: {self.observation}"

if __name__ == "__main__":
    
    # sg1 = StudentsGrades(1244412, 1, 8.5, 0.0, "No Observation")
    # sg2 = StudentsGrades(1244412, 2, 8.5, 0.0, "No Observation")
    # StudentsGrades.save_instance(sg1)
    # StudentsGrades.save_instance(sg2)

    # StudentsGrades.delete_by_id(3)

    # sgUp = StudentsGrades.get_instance(2)
    # sgUp.grade = 7.5
    # sgUp.extra_point = 1.0
    # StudentsGrades.update_instance(sgUp)

    # print(StudentsGrades.get_instance(2))
    
    for each in StudentsGrades.get_all():
        print(each)