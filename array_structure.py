from base_structure import *
from data import *

class ArrayStructure(BaseStructure):
    def __init__(self, max:int) -> None:
        self.records=[None]*max
        self.last_index=0

    def add(self, record:Data) -> None:
        self.records[self.last_index] = record
        self.last_index+=1

    def find(self, key:str) -> str:
        for i in range(0,len(self.records)):
            if self.records[i].key == key:
                return self.records[i].value
        return None

