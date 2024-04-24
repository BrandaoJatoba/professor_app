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

    
    # @classmethod
    # def is_there_class(cls, id:int) -> bool:
    #     if(cls.connection.read("*", cls.table, f"WHERE id = {id}").fetchone()):
    #         return True
    #     return False

    # @classmethod
    # def get_class(cls, id: int) -> "Class":
    #     if Class.is_there_class(id):
    #         info = Class.connection.read("*", Class.table, f"WHERE id = {id}").fetchone()
    #         return Class(info[1], ClassType(int(info[2])), date.fromisoformat(info[3]), info[4], info[5], info[6], info[7], info[0])
    #     return
    
    # @classmethod
    # def save_class(cls, a_class: "Class") -> None:
    #     date = a_class.date.strftime("%Y-%m-%d")
    #     insert_query = {Class.table_row_2: a_class.course_id, Class.table_row_3: ClassType(a_class.class_type).value, Class.table_row_4: date, Class.table_row_5: a_class.subject, Class.table_row_6: a_class.observation, Class.table_row_7: a_class.credit_hours, Class.table_row_8: a_class.was_held}
    #     Class.connection.insert(Class.table, insert_query)
    #     return

    # # HERE!
    # @classmethod
    # def update_class(cls, a_class: "Class") -> None:
    #     date = a_class.date.strftime("%Y-%m-%d")
    #     update_query = f"({Class.table_row_2}, {Class.table_row_3}, {Class.table_row_4}, {Class.table_row_5}, {Class.table_row_6}, {Class.table_row_7}, {Class.table_row_8}) = ({a_class.course_id}, {ClassType(a_class.class_type).value}, '{date}', '{a_class.subject}', '{a_class.observation}', {a_class.credit_hours}, {a_class.was_held})"
    #     Class.connection.update(update_query, Class.table, f" WHERE {Class.table_row_1} = {a_class.id}")
    #     return

    # @classmethod
    # def delete_class(cls, a_class: "Class") -> None:
    #     delete_query = f"{Class.table_row_1} = {a_class.id}"
    #     Class.connection.delete(Class.table, delete_query)
    #     return
    
    # @classmethod
    # def get_all_instances(cls) -> list["Class"]:
    #     list_of_classes = []
    #     info = Class.connection.read("*", Class.table).fetchall()
    #     for a_class in info:
    #         list_of_classes.append(Class(a_class[1], ClassType(int(a_class[2])), date.fromisoformat(a_class[3]), a_class[4], a_class[5], a_class[6], a_class[7], a_class[0]))
    #     return list_of_classes

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
    class_4 = Class.get_instance(5)
    print(class_4)
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
    # for each in Class.get_all():
    #     print(each) 
    ...