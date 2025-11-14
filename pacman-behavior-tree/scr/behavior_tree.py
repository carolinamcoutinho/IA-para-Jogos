from nodes.composite_nodes import Selector, Sequence
from nodes.condition_nodes import *
from nodes.action_nodes import *

def build_behavior_tree(pacman):
    root = Selector(children=[
        Sequence(children=[
            IsGhostVisible(pacman),
            NotHasPower(pacman),
            FleeFromGhost(pacman)
        ]),
        Sequence(children=[
            HasPower(pacman),
            IsGhostVisible(pacman),
            ChaseGhost(pacman)
        ]),
        Sequence(children=[
            PelletsRemaining(pacman),
            PathClear(pacman),
            CollectPellet(pacman)
        ]),
        Sequence(children=[
            Explore(pacman)
        ])
    ])
    return root
