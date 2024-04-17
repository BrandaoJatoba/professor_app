from db_getter import Db_getter

class Teacher(Db_getter):

    table = "teachers"
    table_row_1 = "id"
    table_row_2 = "name"
    table_row_3 = "info"

    def __init__(self, id, name, info):
        self.id = id
        self.name = name
        self.info = info
    
    @classmethod
    def is_there_teacher(cls, id:int) -> bool:
        if(Teacher.connection.read("*", Teacher.table, f"WHERE id = {id}").fetchone()):
            return True
        return False

    @classmethod
    def get_teacher(cls, id: int) -> "Teacher":
        if Teacher.is_there_teacher(id):
            info = Teacher.connection.read("*", Teacher.table, f"WHERE id = {id}").fetchone()
            return Teacher(info[0], info[1], info[2])
        return
    
    @classmethod
    def save_teacher(cls, teacher: "Teacher") -> None:
        insert_query = vars(teacher)
        Teacher.connection.insert(Teacher.table, insert_query)
        return

    @classmethod
    def update_teacher(cls, teacher: "Teacher") -> None:
        update_query = f"({Teacher.table_row_2}, {Teacher.table_row_3}) = ('{teacher.name}', '{teacher.info}')"
        Teacher.connection.update(update_query, Teacher.table, f" WHERE {Teacher.table_row_1} = {teacher.id}")
        return

    @classmethod
    def delete_teacher(cls, teacher: "Teacher") -> None:
        delete_query = f"{Teacher.table_row_1} = {teacher.id}"
        Teacher.connection.delete(Teacher.table, delete_query)
        return



    
if __name__ == "__main__":
    # t1 = Teacher(2, "Fábio", "Cara legal")
    # Teacher.save_teacher(t1)
    # sT1 = Teacher.is_there_teacher(2)
    # print(sT1)
    # Teacher.delete_teacher(t1)
    # sT1 = Teacher.is_there_teacher(2)
    # print(sT1)
    pass