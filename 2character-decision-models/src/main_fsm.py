from character import Geralt

class State:
    def execute(self, geralt):
        raise NotImplementedError

class ExploreState(State):
    def execute(self, geralt):
        if geralt.enemy_visible:
            return CombatState()
        geralt.explore()
        return self

class CombatState(State):
    def execute(self, geralt):
        if geralt.low_health():
            return HealState()
        if geralt.being_attacked:
            geralt.dodge()
        else:
            geralt.attack_enemy()
        # remain in combat unless enemy gone
        if not geralt.enemy_visible:
            return ExploreState()
        return self

class HealState(State):
    def execute(self, geralt):
        geralt.use_potion()
        return ExploreState()

class GeraltFSM:
    def __init__(self, geralt):
        self.state = ExploreState()
        self.geralt = geralt

    def update(self):
        self.state = self.state.execute(self.geralt)

if __name__ == "__main__":
    g = Geralt()
    fsm = GeraltFSM(g)
    # simulate
    g.enemy_visible = True
    fsm.update()
    g.being_attacked = True
    fsm.update()
    g.hp = 30
    fsm.update()
    print("Log FSM:")
    for e in g.log:
        print("-", e)
