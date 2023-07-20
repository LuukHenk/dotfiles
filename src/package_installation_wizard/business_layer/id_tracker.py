from threading import Lock
from typing import List

from logger.logger import log_error


class IdTracker:
    def __init__(self):
        self.__ids = []
        self.__lock = Lock()

    @property
    def ids(self) -> List[int]:
        return self.__ids

    def add_id(self, id_: int) -> None:
        with self.__lock:
            if id_ in self.__ids:
                log_error(f"ID {id_} can't be added. Found a duplicate.")
                return
            self.__ids.append(id_)

    def remove_id(self, id_: int) -> None:
        with self.__lock:
            if id_ not in self.__ids:
                log_error(f"ID {id_} can't be removed. Not found.")
                return
            self.__ids.remove(id_)
