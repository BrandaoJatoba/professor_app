from dbgetter import DbGetter
import json

class Course(DbGetter):

    table = "courses"
    columns = [ "id", #0
                "title", #1 
                "teacher_id", #2
                "schedule", #3
                "info", #4
                "total_credit_hours", #5
                "finished"] #6
    instantiation_attr_order = [1, 2, 5, 3, 4, 6, 0]
    instantiation_attr_types = [str, int, float, dict[str], str, int, int]

    def __init__(self, title: str, teacher_id: int, total_credit_hours: float, schedule: dict[str, str] = {}, info: str = "", finished: int = 0, id: int = -1,) -> None:
        self.id = id
        self.title = title
        self.teacher_id = teacher_id
        self.schedule = schedule
        self.info = info
        self.total_credit_hours = total_credit_hours
        self.finished = finished
    
    def __str__(self):
        if self.finished:
            finished_str = "Ended"
        elif self.finished == False:
            finished_str = "Ongoing"
        return f"Course Id:{self.id}, Title:{self.title}, Teacher:{self.teacher_id}, Schedule: {self.schedule}, Information: {self.info}, Total Credit Hours: {self.total_credit_hours}, Status: {finished_str}"

if __name__ == "__main__":
    c1 = Course("Semiótica", 1, 145.0, {'Friday': "10:00", 'Monday': "11:00"}, "Whatever")
    c2 = Course("Oficina de Rredes", 0, 120.0)
    Course.save_instance(c1)
    Course.save_instance(c2)
    # Course.delete_by_id(5)
    # c3 = Course.get_instance(9)
    # # print(c3)
    # c3.schedule = {"Monday": "10:00", "Tuesday": "10:00"}
    # Course.update_instance(c3)
    for each in Course.get_all():
        print(each)
    # print(Course.is_there_course(1))
    # print(Course.is_there_course(9))
