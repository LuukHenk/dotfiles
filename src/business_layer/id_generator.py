from threading import Lock

from business_layer.singleton import singleton


@singleton
class IdGenerator:
    def __init__(self):
        self.__lock = Lock()
        self.__id = 0

    def generate_id(self) -> int:
        with self.__lock:
            generated_id = self.__id
            self.__id += 1
        return generated_id
