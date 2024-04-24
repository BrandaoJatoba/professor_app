from database import Database
from datetime import date, datetime
from enum import Enum
import enum
import json

class DbGetter:

    connection: Database = Database()
    table: str = ""
    columns: list[str] = []
    instantiation_attr_order: list[int] = []
    instantiation_attr_types = []

    def __init__(self):
        pass
    
    @classmethod
    def is_there_instance(cls, id: int) -> bool:
        if(cls.connection.read("*", cls.table, f"WHERE id = {id}").fetchone()):
            return True
        return False

    @classmethod
    def save_instance(cls, instance: type["DbGetter"]) -> None:
        
        insert_query: dict[str] = {}
        
        for attribute_name in vars(instance):
            
            if isinstance(getattr(instance, attribute_name), Enum):
                insert_query[attribute_name] = getattr(instance, attribute_name).value

            elif isinstance(getattr(instance, attribute_name),datetime):

                date = getattr(instance, attribute_name)      

                insert_query[attribute_name] = date.strftime("%Y-%m-%d")

            elif isinstance(getattr(instance, attribute_name), dict):

                insert_query[attribute_name] = json.dumps(getattr(instance, attribute_name))

            elif (attribute_name == "id") and (getattr(instance, attribute_name) == -1):
                continue
            
            else:
                insert_query[attribute_name] = getattr(instance, attribute_name)
        
        cls.connection.insert(cls.table, insert_query)
        return

    @classmethod
    def get_instance(cls, id: int) -> type["DbGetter"]:
        if cls.is_there_instance(id):

            query_result = cls.connection.read("*", cls.table, f"WHERE id = {id}").fetchone()

            list_of_parameters = []

            for index in range(len(cls.columns)):
                    if cls.instantiation_attr_types[index] == int:
                        list_of_parameters.append(query_result[cls.instantiation_attr_order[index]])
                        continue
                    
                    elif issubclass(cls.instantiation_attr_types[index], enum.Enum):
                        
                        instance_enum = next(member for member in cls.instantiation_attr_types[index] if member.value == query_result[cls.instantiation_attr_order[index]])

                        list_of_parameters.append(instance_enum)
                        
                        continue
                    
                    elif (cls.instantiation_attr_types[index] == datetime):
                        str_to_date = date.fromisoformat(query_result[cls.instantiation_attr_order[index]])
                        list_of_parameters.append(str_to_date)
                        continue
                    
                    elif (cls.instantiation_attr_types[index] == dict[str]):
                        list_of_parameters.append(json.loads(query_result[cls.instantiation_attr_order[index]]))
                        continue

                    else:
                        list_of_parameters.append(query_result[cls.instantiation_attr_order[index]])
                        continue
                    continue

            return  cls(*list_of_parameters)

    @classmethod
    def update_instance(cls, instance:type["DbGetter"]) -> None:
        
        columns_to_update: str = ""
        values_to_update: str = ""
        
        for attribute_name in vars(instance):
            
            if isinstance(getattr(instance, attribute_name), int):
                columns_to_update += attribute_name + ", "
                values_to_update += str(getattr(instance, attribute_name)) + ", "
                continue
            
            if isinstance(getattr(instance, attribute_name), Enum):
                columns_to_update += attribute_name + ', '
                values_to_update += str(getattr(instance, attribute_name).value) + ", " 
                continue

            elif isinstance(instance, datetime):
                date = getattr(instance, attribute_name)      
                columns_to_update += attribute_name + ', '
                values_to_update += "'" + date.strftime("%Y-%m-%d") + "', "
                continue

            elif isinstance(getattr(instance, attribute_name), dict):
                columns_to_update += attribute_name + ', '
                values_to_update += "'" + json.dumps(getattr(instance, attribute_name)) + "', "

            elif (attribute_name == "id") and (getattr(instance, attribute_name) == -1):
                continue
            
            else:

                columns_to_update += attribute_name + ', '
                values_to_update += "'" + str(getattr(instance, attribute_name)) + "', "
                continue

        update_query = "(" + columns_to_update[:-2] + ") = ("+ values_to_update[:-2] +")"

        id_str = "id"

        condition = f"WHERE id = {getattr(instance, id_str)}"
        
        cls.connection.update(update_query, cls.table, condition)

    @classmethod
    def delete_by_id(cls, id: int):
        delete_query = f"id = {id}"
        cls.connection.delete(cls.table, delete_query)
        return

    @classmethod
    def get_all(cls) -> list["DbGetter"]:
        list_of_instances: list["DbGetter"] = []
        
        query_result = cls.connection.read("*", cls.table).fetchall()

        if query_result != []:
            for instance in query_result:
                list_of_parameters = []
                for index in range(len(cls.instantiation_attr_order)):
                    if cls.instantiation_attr_types[index] == int:
                        list_of_parameters.append(instance[cls.instantiation_attr_order[index]])
                        continue
                    
                    elif issubclass(cls.instantiation_attr_types[index], enum.Enum):
                        
                        instance_enum = next(member for member in cls.instantiation_attr_types[index] if member.value == instance[cls.instantiation_attr_order[index]])

                        list_of_parameters.append(instance_enum)
                        
                        continue
                    
                    elif (cls.instantiation_attr_types[index] == datetime):
                        str_to_date = date.fromisoformat(instance[cls.instantiation_attr_order[index]])
                        list_of_parameters.append(str_to_date)
                        continue

                    else:
                        list_of_parameters.append(instance[cls.instantiation_attr_order[index]])
                        continue
                    continue
                list_of_instances.append(cls(*list_of_parameters))
        return list_of_instances
