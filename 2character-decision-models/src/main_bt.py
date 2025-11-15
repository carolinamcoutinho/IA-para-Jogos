from bt.composite_nodes import Selector, Sequence
from bt.base_node import BaseNode
from bt.action_nodes import ActionNode
from bt.condition_nodes import ConditionNode
from character import Geralt

# wrap character's methods into node functions
def build_geralt_bt(geralt):
    def low_health(bb):
        return geralt.low_health()

    def use_potion_action(bb):
        geralt.use_potion()

    def enemy_visible(bb):
        return geralt.enemy_visible_fn()

    def being_attacked(bb):
        return geralt.being_attacked_fn()

    def dodge_action(bb):
        geralt.dodge()

    def attack_action(bb):
        geralt.attack_enemy()

    def explore_action(bb):
        geralt.explore()

    bt = Selector(children=[
        Sequence(children=[ConditionNode(low_health,"LowHealth?"), ActionNode(use_potion_action,"UsePotion")], name="HealSeq"),
        Sequence(children=[
            ConditionNode(enemy_visible,"EnemyVisible?"),
            Selector(children=[
                Sequence(children=[ConditionNode(being_attacked,"BeingAttacked?"), ActionNode(dodge_action,"Dodge")]),
                ActionNode(attack_action,"Attack")
            ])
        ], name="CombatSeq"),
        ActionNode(explore_action,"Explore")
    ], name="GeraltRoot")
    return bt

if __name__ == "__main__":
    g = Geralt()
    bt = build_geralt_bt(g)
    # simulate scenarios
    g.enemy_visible = True
    bt.run({})
    g.being_attacked = True
    bt.run({})
    g.hp = 30
    bt.run({})
    print("\nLog BT:")
    for l in g.log:
        print("-", l)
