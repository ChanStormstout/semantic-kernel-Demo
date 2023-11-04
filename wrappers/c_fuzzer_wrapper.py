import re
from FuzzerAbstractBase import FuzzerAbstractBase
from knowledge_receiver import KnowledgeReceiver


class CFuzzerWrapper(FuzzerAbstractBase):
    def __init__(self, language_type):
        self._language_type = language_type
        # An instance of creating a knowledge receiver
        self.knowledge_receiver = KnowledgeReceiver()

    @property
    def fuzzer_set_up(self):
        return self._language_type
    
    @fuzzer_set_up.setter
    def fuzzer_set_up(self, language_type):
        self._language_type = language_type
    
    def collect_knowledge(self):
        # 调用KnowledgeReceiver的方法来接收用户输入的知识数据
        self.knowledge_receiver.receive_document()
        self.knowledge_receiver.receive_source_code()
        self.knowledge_receiver.receive_use_case()
        # ... 处理收集到的知识数据 ...

    # 下面创建一个CFuzzerWrapper实例并传递知识
c_fuzzer = CFuzzerWrapper(language_type='C/C++')
c_fuzzer.collect_knowledge()
print(c_fuzzer.knowledge_receiver.document_content)

