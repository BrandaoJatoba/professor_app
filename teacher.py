from dbgetter import DbGetter

class Teacher(DbGetter):

    table = "teachers"
    columns: list[str]  =   [
                            "id",
                            "name",
                            "info"
                            ]
    instantiation_attr_order: list[int] = [0, 1, 2]
    instantiation_attr_types = [str, str, int]

    def __init__(self, id: int, name: str, info: str):
        self.id = id
        self.name = name
        self.info = info

    def __str__(self):
        return f"Teacher Id:{self.id}, Name: {self.name}, Information: {self.info}"
    
if __name__ == "__main__":

    # teacher1 = Teacher("Fábio", "Arquitetura")
    # Teacher.save_instance(teacher1)

    # Teacher.delete_by_id(2)

    # updateTeacher = Teacher.get_instance(0)
    # updateTeacher.name = "Jozefh"
    # updateTeacher.info = "Letras"
    # Teacher.update_instance(updateTeacher)

    # print(Teacher.get_instance(0))

    for each in Teacher.get_all():
        print(each)

    # print(Teacher.is_there_instance(2))