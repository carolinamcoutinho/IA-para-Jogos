from abc import ABC, abstractmethod

class NodeStatus:
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    RUNNING = "RUNNING"

class BaseNode(ABC):
    def __init__(self, name=None):
        self.name = name or self.__class__.__name__

    @abstractmethod
    def run(self, blackboard):
        pass

