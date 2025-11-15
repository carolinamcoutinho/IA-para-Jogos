# Minimal environment simulator for Pac-Man BT demo
def initial_blackboard():
    return {
        "pos": (0,0),
        "ghost_pos": (5,5),
        "ghost_visible": False,
        "power_active": False,
        "pellets": 5,
        "score": 0,
        "safe_pos": (0,0),
        "log": []
    }
