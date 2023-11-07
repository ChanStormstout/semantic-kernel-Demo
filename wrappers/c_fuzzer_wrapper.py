import re
from FuzzerAbstractBase import FuzzerAbstractBase
from knowledge_receiver import KnowledgeReceiver


class CFuzzerWrapper(FuzzerAbstractBase):
    def __init__(self, language_type):
        self._language_type = language_type
        # An instance of creating a knowledge receiver
        self.knowledge_receiver = KnowledgeReceiver(doc_file='/home/victor/workspace/semantic-kernel-Demo/wrappers/document.txt', 
                                                    source_code_file='/home/victor/workspace/semantic-kernel-Demo/wrappers/source_code.txt', 
                                                    use_case_file='/home/victor/workspace/semantic-kernel-Demo/wrappers/use_case.txt')

    @property
    def fuzzer_set_up(self):
        return self._language_type
    
    @fuzzer_set_up.setter
    def fuzzer_set_up(self, language_type):
        self._language_type = language_type
    
    def collect_knowledge(self):
        # 调用KnowledgeReceiver的方法来接收用户输入的知识数据
        self.knowledge_receiver.get_dependencies()
        # ... 处理收集到的知识数据 ...



