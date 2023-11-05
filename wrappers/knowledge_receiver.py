import re
import extract_info
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

    def receive_document(self):
        self.document_content = input("请输入文档内容: ")

    def receive_source_code(self):
        self.source_code = input("请输入源代码: ")
    
    def receive_use_case(self):
        self.use_case = input("请输入使用案例: ")
    
    # todo: _create_summary should use SK framework to return the summary of target function.
    def func_summarizer(self):
        summary = self._create_summary(self.source_code)
        return summary
    def _create_summary(self, text):
        return text[:100]
    
    # TODO: extract the information of dependencies
    def get_dependencies(self):
        self.dependencies = extract_info.extract_dependencies_from_file()
