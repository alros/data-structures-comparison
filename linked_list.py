from base_structure import *
from data import *

class LinkedList(BaseStructure):
    class Entry:
        def __init__(self, record:Data) -> None:
            self.record = record
            self.next = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, record:Data) -> None:
        entry = self.Entry(record)
        if self.head is None:
            self.head = entry
            self.tail = self.head
        else:
            self.tail.next = entry
            self.tail = self.tail.next

    def find(self, key:str) -> str:
        cur = self.head
        while cur is not None and cur.record.key != key:
            cur = cur.next
        return cur.record.value if cur is not None else None
