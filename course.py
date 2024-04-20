"""
     TO DO 
     insert boolean (zero and one) field to finished column
     make method to change finished field and update db

"""

from db_getter import Db_getter
import json

class Course(Db_getter):

    table = "courses"
    table_row_1 = "id"
    table_row_2 = "title"
    table_row_3 = "teacher_id"
    table_row_4 = "schedule"
    table_row_5 = "info"
    table_row_6 = "finished"

    #list_of_courses = []

    def __init__(self, title: str, teacher_id: int,  schedule: dict[str, str] = {}, info: str = "", id: int = -1, finished: int = 0) -> None:
        self.id = id
        self.title = title
        self.teacher_id = teacher_id
        self.schedule = schedule
        self.info = info
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
            return Course(info[1], info[2], json.loads(info[3]), info[4], info[0], info[5])
        return
    
    @classmethod
    def save_course(cls, course: "Course") -> None:
        insert_query = {Course.table_row_2: course.title, Course.table_row_3: course.teacher_id, Course.table_row_4: json.dumps(course.schedule), Course.table_row_5: course.info, Course.table_row_6: course.finished}
        Course.connection.insert(Course.table, insert_query)
        return

    # HERE!
    @classmethod
    def update_course(cls, course: "Course") -> None:
        update_query = f"({Course.table_row_2}, {Course.table_row_3}, {Course.table_row_4}, {Course.table_row_5}, {Course.table_row_6}) = ('{course.title}', {course.teacher_id}, '{json.dumps(course.schedule)}', '{course.info}', {course.finished})"
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
            list_of_courses.append(Course(course[1], course[2], json.loads(course[3]), course[4], course[0], course[5]))
        return list_of_courses

    def __str__(self):
        if self.finished:
            finished_str = "Ended"
        elif self.finished == False:
            finished_str = "Ongoing"
        return f"Course Id:{self.id}, Title:{self.title}, Teacher:{self.teacher_id}, Schedule: {self.schedule}, Information: {self.info}, Status: {finished_str}"

if __name__ == "__main__":
    # c1 = Course("Calculus", 1, {'Friday': "10:00", 'Monday': "11:00"}, "Something Something Something")
    # c2 = Course("Laboratório de Programação", 0)
    # Course.save_course(c1)
    # Course.save_course(c2)
    # Course.delete_course(Course("ajsidjai", 1))
    # Course.delete_by_id(2)
    # c1 = Course.get_course(3)
    # c1.title = "DMing with grace"
    # c1.teacher_id = 0
    # Course.update_course(c1)
    for each in Course.get_all_instances():
        print(each)
    # print(Course.is_there_course(1))
    # print(Course.is_there_course(9))
