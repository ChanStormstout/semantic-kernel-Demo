import os
from abc import ABC, abstractmethod
class KnowledgeBase(ABC):  
    
    @property
    @abstractmethod
    def func_summarizer(self, text):
        """Abstract method to summarize a piece of text."""
        pass


# TODO: add the dependency info
    @property
    @abstractmethod
    def get_dependencies(self):
        """Extract the information of dependencies"""
        pass
    @get_dependencies.setter
    @abstractmethod
    def get_dependencies(self, dep_info: str):
        pass