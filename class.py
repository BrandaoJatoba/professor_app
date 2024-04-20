from db_getter import Db_getter
from classType import ClassType

class Class(Db_getter):

    table = "classes"
    table_row_1 = "id"
    table_row_2 = "course_id"
    table_row_3 = "type"
    table_row_4 = "date"
    table_row_5 = "info"
    table_row_6 = "observation"
    table_row_7 = "was_held"
        
    def __init__(self, course_id: int, class_type: ClassType, date: str, subject: str, observation: str, was_held: int = 0, id: int = -1) -> None:
        self.id = id
        self.course_id = course_id
        self.date = date
        self.class_type = class_type
        self.subject = subject
        self.observation = observation
        self.was_held = was_held

    
    @classmethod
    def is_there_class(cls, id:int) -> bool:
        if(cls.connection.read("*", cls.table, f"WHERE id = {id}").fetchone()):
            return True
        return False

    @classmethod
    def get_class(cls, id: int) -> "Class":
        if Class.is_there_class(id):
            info = Class.connection.read("*", Class.table, f"WHERE id = {id}").fetchone()
            return Class(info[1], info[2], info[3], info[4], info[5], info[6], info[0])
        return
    
    @classmethod
    def save_class(cls, a_class: "Class") -> None:
        insert_query = {Class.table_row_2: a_class.course_id, Class.table_row_3: a_class.class_type, Class.table_row_4: a_class.date, Class.table_row_5: a_class.subject, Class.table_row_6: a_class.observation, Class.table_row_7: a_class.was_held}
        Class.connection.insert(Class.table, insert_query)
        return

    # HERE!
    @classmethod
    def update_class(cls, a_class: "Class") -> None:
        update_query = f"({Class.table_row_2}, {Class.table_row_3}, {Class.table_row_4}, {Class.table_row_5}, {Class.table_row_6}, {Class.table_row_7}) = ({a_class.course_id}, '{a_class.class_type}', '{a_class.date}', '{a_class.subject}', '{a_class.observation}', {a_class.was_held})"
        Class.connection.update(update_query, Class.table, f" WHERE {Class.table_row_1} = {a_class.id}")
        return

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
            list_of_classes.append(Class(a_class[1], a_class[2], a_class[3], a_class[4], a_class[5], a_class[6], a_class[0]))
        return list_of_classes

    def __str__(self):
        if self.was_held:
            held_str = "Held"
        elif self.was_held == False:
            held_str = "Not held"
        return f"Class Id:{self.id}, Course Id:{self.course_id}, Type:{self.class_type}, Date: {self.date}, Subject: {self.subject}, Observation: {self.observation}, Status: {self.was_held}"

if __name__ == "__main__":
    # class_1 = Class(1, ClassType.COMUM, '15/05/2024', "Pré-Cálculo", "")
    # class_2 = Class(1, ClassType.COMUM, '15/05/2024', "Limites", "")
    # class_3 = Class(1, ClassType.COMUM, '15/05/2024', "Área sobre a curva", "")
    # Class.save_class(class_1) 
    # Class.save_class(class_2) 
    # Class.save_class(class_3)
    # class_4 = Class.get_class(2)
    # class_4.date = "22/05/2024"
    # Class.update_class(class_4)
    # Class.delete_by_id(2)
    for each in Class.get_all_instances():
        print(each) 
    