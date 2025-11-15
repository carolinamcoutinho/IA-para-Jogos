from .base_node import BaseNode, NodeStatus

class ActionNode(BaseNode):
    def __init__(self, action_fn, name=None):
        super().__init__(name)
        self.action_fn = action_fn

    def run(self, bb):
        try:
            self.action_fn(bb)
            return NodeStatus.SUCCESS
        except Exception as e:
            print(f"Action {self.name} failed: {e}")
            return NodeStatus.FAILURE

# actions (example implementations operating on the blackboard)
def flee_action(bb):
    bb['log'].append("Pac-Man flees from ghost")
    # simplistic move change
    bb['pos'] = bb.get('safe_pos', bb.get('pos'))

def chase_action(bb):
    bb['log'].append("Pac-Man chases ghost")
    bb['pos'] = bb.get('ghost_pos', bb.get('pos'))

def collect_pellet_action(bb):
    if bb.get('pellets',0) > 0:
        bb['pellets'] -= 1
        bb['score'] = bb.get('score',0) + 10
        bb['log'].append("Pac-Man collected a pellet")
    else:
        raise RuntimeError("no pellets")

def explore_action(bb):
    bb['log'].append("Pac-Man explores")
    bb['pos'] = bb.get('pos')  # in real case, change pos
