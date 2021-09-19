from base_structure import *
from data import *

class BTree(BaseStructure):
    class Node:
        def __init__(self, value:Data) -> None:
            self.left = None
            self.right = None
            self.value = value

    def __init__(self) -> None:
        self.head = None
    
    def add(self, record:Data) -> None:
        node = self.Node(record)
        if(self.head is None):
            self.head = node
        else:
            self.__add(node, self.head)

    def __add(self, node:Node, head:Node) -> None:
            if head.value.key > node.value.key:
                if head.right is None:
                    head.right = node
                else:
                    self.__add(node, head.right)
            else:
                if head.left is None:
                    head.left = node
                else:
                    self.__add(node, head.left)
    
    def find(self, key:str) -> str:
        return self.__find(key, self.head)

    def __find(self, key:str, head:Node) -> str:
        if head is None:
            return None
        elif head.value.key == key:
            return head.value.value
        elif head.value.key < key:
            return self.__find(key, head.left)
        else:
            return self.__find(key, head.right)
