class Geralt:
    def __init__(self):
        self.hp = 100
        self.stamina = 100
        self.enemy_visible = False
        self.being_attacked = False
        self.position = (0,0)
        self.log = []

    # sensor helpers
    def low_health(self):
        return self.hp < 40

    def enemy_visible_fn(self):
        return self.enemy_visible

    def being_attacked_fn(self):
        return self.being_attacked

    # actions
    def use_potion(self):
        self.hp = min(100, self.hp + 50)
        self.log.append("Geralt used a potion")

    def dodge(self):
        self.log.append("Geralt dodged an attack")

    def attack_enemy(self):
        self.log.append("Geralt attacked enemy")

    def explore(self):
        self.log.append("Geralt explores")