import os
from abc import ABC, abstractmethod
class KnowledgeBase(ABC):
    
    @property
    @abstractmethod
    def extract_knowledge(self):
        pass

    @extract_knowledge.setter
    @abstractmethod
    def extract_knowledge(self, func_info):
        pass
    
    @property
    @abstractmethod
    def func_summarizer(self, text):
        """Abstract method to summarize a piece of text."""
        pass

    @abstractmethod    
    def receive_source_code(self, source_code: str):
        """Receive and process the source code."""
        pass
    
    @property
    @abstractmethod
    def receive_document(self):
        """Receive and process the related documents' content"""
        pass
    @receive_document.setter
    @abstractmethod
    def receive_document(self, document_content: str):
        pass

    @property
    @abstractmethod
    def receive_use_case(self):
        """Receive and process the use case of the function"""
        pass
    @receive_use_case.setter
    @abstractmethod
    def receive_use_case(self, use_case: str):        
        pass

# TODO: add the dependency info
    @property
    @abstractmethod
    def dependencies(self):
        """Extract the information of dependencies"""
        pass
    @dependencies.setter
    @abstractmethod
    def get_dependencies(self, dep_info: str):
        pass