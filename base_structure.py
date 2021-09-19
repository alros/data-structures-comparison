from abc import abstractmethod, ABCMeta
from data import *

class BaseStructure(metaclass=ABCMeta):

    @abstractmethod
    def add(self, record:Data) -> None:
        '''
        Init the data with n records and stores a 'sample' to be used in find
        '''
        pass

    @abstractmethod
    def find(self, key:str) -> str:
        '''
        Find the 'sample' created in the init
        '''
        pass

