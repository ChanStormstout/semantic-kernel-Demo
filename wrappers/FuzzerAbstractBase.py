from abc import ABC, ABCMeta, abstractmethod
from KnowledgeReceiverBase import KnowledgeBase
class FuzzerAbstractBase(ABC):
    def __init__(self):
         self._target_function = None
    @property
    @abstractmethod
    def fuzzer_set_up(self):
        pass

    @fuzzer_set_up.setter
    @abstractmethod
    def fuzzer_set_up(self, language_tpye):
        pass

    @property
    @abstractmethod
    def target_function(self):
        pass

    @target_function.setter
    @abstractmethod
    def target_function(self, value):
        pass
