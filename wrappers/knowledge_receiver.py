import re
import extract_info
from KnowledgeReceiverBase import KnowledgeBase

class KnowledgeReceiver(KnowledgeBase):
    def __init__(self, doc_file, source_code_file, use_case_file):
        self.document_content = self._read_file(doc_file)
        self.source_code = self._read_file(source_code_file)
        self.use_case = self._read_file(use_case_file)
        self.dependencies = ""

    # Add the _read_file method here
    def _read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return ""

    # def receive_document(self, text: str):
    #     self.document_content = input("请输入文档内容: ")

    # def receive_source_code(self, source_code: str):
    #     self.source_code = source_code
    
    # def receive_use_case(self, use_case: str):
    #     self.use_case = use_case
    
    # todo: _create_summary should use SK framework to return the summary of target function.
    def func_summarizer(self):
        summary = self._create_summary(self.source_code)
        return summary
    def _create_summary(self, text):
        return text[:100]
    
    # TODO: extract the information of dependencies
    def get_dependencies(self):
        self.dependencies = extract_info.get_dependencies('ares_create_query.c')
