from typing import List, Optional, Dict
from dataclasses import fields

from data_models.manager import Manager
from data_models.object import Object
from data_models.result import Result
from data_models.accessor_result_message import AccessorResultMessage as ResultMessage


class Accessor:
    def __init__(self):
        self.__objects: Dict[int, Object] = {}

    def find_object_via_bk(self, search_name: str, manager: Manager) -> Optional[Object]:
        """Use the business keys to find the object. This will take longer then finding the object via the PK"""
        for object_ in self.__objects.values():
            if object_.manager == manager and object_.search_name == search_name:
                return object_
        return None

    def find_object_via_id(self, object_id: int) -> Optional[Object]:
        """Use the primary key to find the object"""
        try:
            return self.__objects[object_id]
        except KeyError:
            return None

    def add_object(self, search_name: str, manager: Manager) -> Result:
        if self.find_object_via_bk(search_name, manager) is not None:
            return Result(success=False, message=ResultMessage.DUPLICATION)
        object_ = Object(search_name=search_name, manager=manager)
        self.__objects[object_.id_] = object_
        return Result(success=True)

    def update_object(self, object_id: int, updated_object: Object) -> Result:
        object_ = self.find_object_via_id(object_id)
        validation_result = self.__validate_update(object_, updated_object)
        if not validation_result.success:
            return validation_result

        # TODO: #0000001
        self.__objects.search_name = updated_object.search_name
        self.__objects.manager = updated_object.manager
        self.__objects.name = updated_object.name
        self.__objects.group = updated_object.group
        self.__objects.state = updated_object.state

    def __validate_update(self, object_: Optional[Object], updated_object: Object) -> Result:
        if not object_:
            return Result(success=False, message=ResultMessage.NOT_FOUND)
        duplicate = self.find_object_via_bk(updated_object.search_name, updated_object.manager)
        if duplicate is not None:
            if duplicate.id_ == object_.id_:
                return Result(success=False, message=ResultMessage.UNCHANGED)
            else:
                return Result(success=False, message=ResultMessage.DUPLICATION)
        return Result(success=True)


if __name__ == "__main__":
    accessor = Accessor()
    some_object = Object(
        search_name="abc",
    )
