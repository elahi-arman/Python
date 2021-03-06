from abc import ABC, abstractmethod
from collections import namedtuple

class Base(ABC):
    Element = namedtuple('Element', 'semantic string')

    @abstractmethod
    def write(self, filename):
        """Write the current element tree to the given filename."""
        pass
    #
    # @staticmethod
    # def scan(newDoc, oldDoc, spec):
    #     """In memory parses oldDoc according to spec and writes to newDoc."""
    #     pass
