class ActionNode:
    def __init__(self, pacman):
        self.pacman = pacman

    def run(self):
        pass

class FleeFromGhost(ActionNode):
    def run(self):
        print("Pac-Man fugindo do fantasma!")
        self.pacman.move_away_from_ghost()
        return True

class ChaseGhost(ActionNode):
    def run(self):
        print("Pac-Man perseguindo o fantasma!")
        self.pacman.move_toward_ghost()
        return True

class CollectPellet(ActionNode):
    def run(self):
        print("Pac-Man coletando pastilha.")
        self.pacman.collect_pellet()
        return True

class Explore(ActionNode):
    def run(self):
        print("Pac-Man explorando o labirinto.")
        self.pacman.move_randomly()
        return True
