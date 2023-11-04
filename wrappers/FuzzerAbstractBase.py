from abc import ABC, ABCMeta, abstractmethod
from KnowledgeReceiverBase import KnowledgeBase
class FuzzerAbstractBase(ABC):
    @property
    @abstractmethod
    def fuzzer_set_up(self):
        pass

    @fuzzer_set_up.setter
    @abstractmethod
    def fuzzer_set_up(self, language_tpye):
        pass

    @abstractmethod
    def fuzzer_knowledge(self, KnowledgeBase):
        raise NotImplementedError


