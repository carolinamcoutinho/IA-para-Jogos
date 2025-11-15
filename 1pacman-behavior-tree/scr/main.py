from bt.composite_nodes import Selector, Sequence
from bt.condition_nodes import ConditionNode, ghost_visible, has_power, pellets_remaining
from bt.action_nodes import ActionNode, flee_action, chase_action, collect_pellet_action, explore_action
from world import initial_blackboard

def build_tree():
    # Modo defesa: se fantasma visível e sem poder -> fugir
    seq_def = Sequence(children=[
        ConditionNode(lambda bb: ghost_visible(bb), name="GhostVisible?"),
        ConditionNode(lambda bb: not has_power(bb), name="NoPower?"),
        ActionNode(flee_action, name="Flee")
    ], name="DefenseSequence")

    seq_attack = Sequence(children=[
        ConditionNode(lambda bb: has_power(bb), name="HasPower?"),
        ConditionNode(lambda bb: ghost_visible(bb), name="GhostVisible?"),
        ActionNode(chase_action, name="Chase")
    ], name="AttackSequence")

    seq_collect = Sequence(children=[
        ConditionNode(lambda bb: pellets_remaining(bb), name="PelletsRemaining?"),
        ActionNode(collect_pellet_action, name="CollectPellet")
    ], name="CollectSequence")

    seq_explore = Sequence(children=[ActionNode(explore_action, name="Explore")], name="ExploreSeq")

    root = Selector(children=[seq_def, seq_attack, seq_collect, seq_explore], name="RootSelector")
    return root

def simulate(steps=10):
    tree = build_tree()
    bb = initial_blackboard()
    for t in range(steps):
        # For demo: toggle some environment aspects
        if t==1:
            bb['ghost_visible'] = True
        if t==2:
            bb['power_active'] = True
        if t==3:
            bb['ghost_visible'] = False
        tree.run(bb)
    # print logs
    print("Log:")
    for entry in bb['log']:
        print("-", entry)
    print("Final score:", bb['score'])

if __name__ == "__main__":
    simulate(steps=6)
