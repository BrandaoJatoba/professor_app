from dbgetter import DbGetter

class Student(DbGetter):
    
    table = "students"    
    columns: list[str]  =   [
                            "id",
                            "name",
                            "observation"
                            ]
    instantiation_attr_order: list[int] = [0, 1, 2]
    instantiation_attr_types = [int, str, str]

    def __init__(self, id, name, observation):
        self.id = id
        self.name = name
        self.observation = observation
    
    def __str__(self) -> str:
        return f"Student Id: {self.id}, Name: {self.name}, Observation: {self.observation}"


if __name__ == "__main__":

    if Student.is_there_instance(1244412) is False:
        st1 = Student(1244412, "João Felipe", "No Observations")
        # st2 = Student(2354123, "Alan", "No Observations")
        Student.save_instance(st1)
        # Student.save_instance(st2)

    # Student.delete_by_id(1244412)

    for each in Student.get_all():
        print(each)