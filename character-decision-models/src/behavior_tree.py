from nodes.composite_nodes import Selector, Sequence
from nodes.condition_nodes import *
from nodes.action_nodes import *

def build_behavior_tree(geralt):
    root = Selector(children=[
        Sequence(children=[
            LowHealth(geralt),
            UsePotion(geralt)
        ]),
        Sequence(children=[
            EnemyVisible(geralt),
            Selector(children=[
                Sequence(children=[BeingAttacked(geralt), Dodge(geralt)]),
                Sequence(children=[StaminaAvailable(geralt), AttackEnemy(geralt)]),
                Defend(geralt)
            ])
        ]),
        Sequence(children=[
            AreaSafe(geralt),
            Explore(geralt)
        ])
    ])
    return root
