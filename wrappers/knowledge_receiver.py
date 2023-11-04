import re
from KnowledgeReceiverBase import KnowledgeBase

class KnowledgeReceiver(KnowledgeBase):
    def __init__(self) -> None:
        self._extract_knowledge_func = None

    @property
    def extract_knowledge(self):
        return self._extract_knowledge_func
    
    @extract_knowledge.setter
    def extract_knowledge(self, func_info):
        self._extract_knowledge_func = func_info
    
    # todo: _create_summary should use SK framework to return the summary of target function.
    def func_summarizer(self, text):
        summary = self._create_summary(text)
        return summary
    def _create_summary(self, text):
        return text[:100]

    def receive_source_code(self, source_code: str):
        return self.receive_source_code(source_code)
    
    def receive_document(self, document_content: str):
        return self.receive_document(document_content)
    
    def receive_use_case(self, use_case: str):
        return self.receive_use_case(use_case)