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

    @abstractmethod
    def receive_document(self, document_content: str):
        """Receive and process the related documents' content"""
        pass
    
    @abstractmethod
    def receive_use_case(self, use_case: str):        
        """Receive and process the use case of the function"""
        pass
