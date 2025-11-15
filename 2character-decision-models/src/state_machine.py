class GeraltState:
    def __init__(self, name):
        self.name = name

    def execute(self, geralt):
        pass


class CombatState(GeraltState):
    def execute(self, geralt):
        if geralt.low_health():
            geralt.change_state(HealState())
        elif geralt.being_attacked():
            geralt.dodge()
        else:
            geralt.attack_enemy()


class HealState(GeraltState):
    def execute(self, geralt):
        geralt.use_potion()
        geralt.change_state(ExploreState())


class ExploreState(GeraltState):
    def execute(self, geralt):
        if geralt.enemy_visible():
            geralt.change_state(CombatState())
        else:
            geralt.explore()


class GeraltFSM:
    def __init__(self, geralt):
        self.current_state = ExploreState()
        self.geralt = geralt

    def update(self):
        print(f"Estado atual: {self.current_state.__class__.__name__}")
        self.current_state.execute(self.geralt)
