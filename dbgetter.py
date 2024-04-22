from database import Database

class DbGetter:

    table = ""
    connection = Database()

    def __init__(self):
        pass
    
    @classmethod
    def is_there_instance(cls, id: int) -> bool:
        if(cls.connection.read("*", cls.table, f"WHERE id = {id}").fetchone()):
            return True
        return False

    @classmethod
    def delete_by_id(cls, id: int):
        delete_query = f"id = {id}"
        cls.connection.delete(cls.table, delete_query)
        return

    # @classmethod
    # def delete_instance(cls, instance) -> None:
    #     delete_query = f"{instance.table_row_1} = {instance.id}"
    #     cls.connection.delete(cls.table, delete_query)
    #     return