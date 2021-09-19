from base_structure import *
from linked_list import *
from data import *

class HashMap(BaseStructure):

    def __init__(self) -> None:
        self.array_size = 31
        self.array = [None]*self.array_size

    def add(self, data:Data):
        hash = self.__hash(data.key)
        if self.array[hash] is None:
            self.array[hash] = LinkedList()
        self.array[hash].add(data)

    def find(self, key:str) -> str:
        hash = self.__hash(key)
        if self.array[hash] is None:
            return None
        else:
            return self.array[hash].find(key)

    def __hash(self, string:str) -> int:
        value = 0
        for element in range(0, len(string)):
            value+=ord(string[element])
        return value%self.array_size