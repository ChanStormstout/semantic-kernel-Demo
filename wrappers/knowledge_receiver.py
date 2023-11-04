import re
from KnowledgeReceiverBase import KnowledgeBase

class KnowledgeReceiver(KnowledgeBase):
    def __init__(self):
        self.document_content = ""
        self.source_code = ""
        self.use_case = ""

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

    def receive_document(self):
        self.document_content = input("请输入文档内容: ")

    def receive_source_code(self):
        self.source_code = input("请输入源代码: ")
    
    def receive_use_case(self):
        self.use_case = input("请输入使用案例: ")