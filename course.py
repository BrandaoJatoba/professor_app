"""
     TO DO 
     insert boolean (zero and one) field to finished column
     make method to change finished field and update db

"""

from dbgetter import DbGetter
import json

class Course(DbGetter):

    table = "courses"
    table_row_1 = "id" #int
    table_row_2 = "title" #str
    table_row_3 = "teacher_id" #int
    table_row_4 = "schedule" #str on the database
    table_row_5 = "info" #str
    table_row_6 = "total_credit_hours" #float
    table_row_7 = "finished" #int

    #list_of_courses = []

    def __init__(self, title: str, teacher_id: int, total_credit_hours: float, schedule: dict[str, str] = {}, info: str = "", id: int = -1, finished: int = 0) -> None:
        self.id = id
        self.title = title
        self.teacher_id = teacher_id
        self.schedule = schedule
        self.info = info
        self.total_credit_hours = total_credit_hours
        self.finished = 0
    
    @classmethod
    def is_there_course(cls, id:int) -> bool:
        if(cls.connection.read("*", cls.table, f"WHERE id = {id}").fetchone()):
            return True
        return False

    @classmethod
    def get_course(cls, id: int) -> "Course":
        if Course.is_there_course(id):
            info = Course.connection.read("*", Course.table, f"WHERE id = {id}").fetchone()
            return Course(info[1], info[2], info[5], json.loads(info[3]), info[4], info[0], info[6])
        return
    
    @classmethod
    def save_course(cls, course: "Course") -> None:
        insert_query = {Course.table_row_2: course.title, Course.table_row_3: course.teacher_id, Course.table_row_4: json.dumps(course.schedule), Course.table_row_5: course.info, Course.table_row_6: course.total_credit_hours, Course.table_row_7: course.finished}
        Course.connection.insert(Course.table, insert_query)
        return

    # HERE!
    @classmethod
    def update_course(cls, course: "Course") -> None:
        update_query = f"({Course.table_row_2}, {Course.table_row_3}, {Course.table_row_4}, {Course.table_row_5}, {Course.table_row_6}, {Course.table_row_7}) = ('{course.title}', {course.teacher_id}, '{json.dumps(course.schedule)}', '{course.info}', {course.total_credit_hours}, {course.finished})"
        Course.connection.update(update_query, Course.table, f" WHERE {Course.table_row_1} = {course.id}")
        return

    @classmethod
    def delete_course(cls, course: "Course") -> None:
        delete_query = f"{Course.table_row_1} = {course.id}"
        Course.connection.delete(Course.table, delete_query)
        return
    
    @classmethod
    def get_all_instances(cls) -> list["Course"]:
        list_of_courses = []
        info = Course.connection.read("*", Course.table).fetchall()
        for course in info:
            list_of_courses.append(Course(course[1], course[2], course[5], json.loads(course[3]), course[4], course[0], course[6]))
        return list_of_courses

    def __str__(self):
        if self.finished:
            finished_str = "Ended"
        elif self.finished == False:
            finished_str = "Ongoing"
        return f"Course Id:{self.id}, Title:{self.title}, Teacher:{self.teacher_id}, Schedule: {self.schedule}, Information: {self.info}, Total Credit Hours: {self.total_credit_hours}, Status: {finished_str}"

if __name__ == "__main__":
    # c1 = Course("Calculus", 1, 145.0, {'Friday': "10:00", 'Monday': "11:00"}, "Something Something Something")
    # c2 = Course("Laboratório de Programação", 0, 120.0)
    # Course.save_course(c1)
    # Course.save_course(c2)
    # Course.save_course(c2)
    # Course.delete_course(Course("ajsidjai", 1))
    # Course.delete_by_id(5)
    # c3 = Course.get_course(3)
    # c3.title = "DMing with grace"
    # c3.teacher_id = 0
    # Course.update_course(c3)
    for each in Course.get_all_instances():
        print(each)
    # print(Course.is_there_course(1))
    # print(Course.is_there_course(9))
