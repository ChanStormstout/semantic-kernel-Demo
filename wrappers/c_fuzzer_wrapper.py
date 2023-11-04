import re
from FuzzerAbstractBase import FuzzerAbstractBase
from knowledge_receiver import KnowledgeReceiver


class c_fuzzer_wrapper(FuzzerAbstractBase):
    def __init__(self, language_type):
        self._language_type = None

    @property
    def fuzzer_set_up(self):
        return self._language_type
    
    @fuzzer_set_up.setter
    def fuzzer_set_up(self, language_type):
        self.language_type = language_type
    
    def fuzzer_knowledge(self, KnowledgeBase):
        return self.fuzzer_knowledge(KnowledgeBase)



receiver = KnowledgeReceiver()
receiver.extract_knowledge("info")
receiver.receive_document("This is a sample document.")
receiver.receive_source_code("sourcode")
receiver.receive_use_case("usecase")
