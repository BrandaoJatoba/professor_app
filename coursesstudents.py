from dbgetter import DbGetter

class CoursesStudents(DbGetter):
    
    table = "courses_students"
    columns =   [
                "id", 
                "student_id", 
                "course_id"
                ]
    instantiation_attr_order = [1, 2, 0]
    instantiation_attr_types = [int, int, int]

    def __init__(self, student_id: int, course_id: int, id: int = -1):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
    
    def __str__(self):
        return f"Aluno {self.student_id} está matriculado no Turma {self.course_id}. Id da matrícula é {self.id}"
    
if __name__ == "__main__":
    # cs1 = CoursesStudents(2354123, 1)
    # cs2 = CoursesStudents(2354123, 2)
    # CoursesStudents.save_instance(cs1)
    # CoursesStudents.save_instance(cs2)

    # CoursesStudents.delete_by_id(4)

    # cs3 = CoursesStudents.get_instance(3)
    # cs3.course_id = 4
    # CoursesStudents.update_instance(cs3)

    # print(CoursesStudents.get_instance(1))

    for each in CoursesStudents.get_all():
        print(each)