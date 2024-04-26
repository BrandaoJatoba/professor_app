from dbgetter import DbGetter
from classType import ClassType
from datetime import date, datetime

class Class(DbGetter):

    table = "classes"
    columns = [
        "id", 
        "course_id", 
        "class_type", 
        "date", 
        "subject", 
        "observation", 
        "credit_hours", 
        "was_held"
        ]
    instantiation_attr_order = [1, 2, 3, 4, 5, 6, 7, 0]
    instantiation_attr_types = [int, ClassType, datetime, str, str, float, int, int]
        
    def __init__(self, course_id: int, class_type: ClassType, date: datetime, subject: str, observation: str, credit_hours: float,was_held: int = 0, id: int = -1) -> None:
        self.id = id
        self.course_id = course_id
        self.date = date
        self.class_type = class_type
        self.subject = subject
        self.observation = observation
        self.credit_hours = credit_hours
        self.was_held = was_held

    def __str__(self):
        if self.was_held:
            held_str = "Held"
        elif self.was_held == False:
            held_str = "Not held"
        d = self.date.strftime("%d %B, %Y")
        return f"Class Id:{self.id}, Course Id:{self.course_id}, Type:{ClassType(self.class_type).value}, Date: {d}, Subject: {self.subject}, Observation: {self.observation}, Class Credit Hours: {self.credit_hours}, Status: {self.was_held}"

if __name__ == "__main__":
    # class_1 = Class(1, ClassType.COMUM.value, date.fromisoformat('2024-05-15'), "Whatever", "", 2.0)
    # class_2 = Class(1, ClassType.COMUM.value, date.fromisoformat('2024-05-22'), "Limites", "", 2.0)
    # class_3 = Class(1, ClassType.COMUM.value, date.fromisoformat('2024-05-31'), "Área sobre a curva", "", 2.0)
    # class_4 = Class(1, ClassType.EXTRA.value, date.fromisoformat('2024-06-11'), "Derivada", "", 2.0)
    # Class.connection.cursor.execute("ALTER TABLE classes RENAME info to subject")
    # Class.save_instance(class_1) 
    # Class.save_instance(class_2) 
    # Class.save_instance(class_3)
    # Class.save_instance(class_4)
    # class_4 = Class.get_instance(5)
    # print(class_4)
    # class_4.subject = "Inclinação da curva"
    # class_4.date = "2024-05-15"
    # Class.update_instance(class_4)
    # Class.delete_by_id(6)
    # Class.delete_by_id(7)
    # Class.delete_by_id(8)
    # class_5 = Class.get_class(3)
    # class_5.class_type = ClassType.COMUM.value
    # # Class.update_class(class_5)
    # print(Class.get_instance(1))
    for each in Class.get_all():
        print(each) 
    ...