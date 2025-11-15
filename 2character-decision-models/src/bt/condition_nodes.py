from .base_node import BaseNode, NodeStatus

class ConditionNode(BaseNode):
    def __init__(self, cond_fn, name=None):
        super().__init__(name)
        self.cond_fn = cond_fn

    def run(self, bb):
        return NodeStatus.SUCCESS if self.cond_fn(bb) else NodeStatus.FAILURE

# helper conditions (examples)
def ghost_visible(bb):
    return bb.get("ghost_visible", False)

def has_power(bb):
    return bb.get("power_active", False)

def pellets_remaining(bb):
    return bb.get("pellets", 0) > 0
