from database import Database

class Db_getter:

    table = ""
    connection = Database()

    def __init__(self):
        pass

    @classmethod
    def delete_by_id(cls, id: int):
        delete_query = f"id = {id}"
        cls.connection.delete(cls.table, delete_query)
        return