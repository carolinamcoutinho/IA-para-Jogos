from .base_node import BaseNode, NodeStatus

class Sequence(BaseNode):
    def __init__(self, children, name=None):
        super().__init__(name)
        self.children = children

    def run(self, bb):
        for c in self.children:
            status = c.run(bb)
            if status != NodeStatus.SUCCESS:
                return status
        return NodeStatus.SUCCESS

class Selector(BaseNode):
    def __init__(self, children, name=None):
        super().__init__(name)
        self.children = children

    def run(self, bb):
        for c in self.children:
            status = c.run(bb)
            if status == NodeStatus.SUCCESS:
                return NodeStatus.SUCCESS
        return NodeStatus.FAILURE
