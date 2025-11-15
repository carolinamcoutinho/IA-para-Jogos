# A* implementation for Romania map (Arad -> Bucharest)
import heapq
from math import inf

# graph (AIMA / standard Romania roads)
GRAPH = {
    'Arad': [('Zerind',75),('Sibiu',140),('Timisoara',118)],
    'Zerind': [('Arad',75),('Oradea',71)],
    'Oradea': [('Zerind',71),('Sibiu',151)],
    'Sibiu': [('Arad',140),('Oradea',151),('Fagaras',99),('Rimnicu Vilcea',80)],
    'Fagaras': [('Sibiu',99),('Bucharest',211)],
    'Rimnicu Vilcea': [('Sibiu',80),('Pitesti',97),('Craiova',146)],
    'Timisoara': [('Arad',118),('Lugoj',111)],
    'Lugoj': [('Timisoara',111),('Mehadia',70)],
    'Mehadia': [('Lugoj',70),('Drobeta',75)],
    'Drobeta': [('Mehadia',75),('Craiova',120)],
    'Craiova': [('Drobeta',120),('Rimnicu Vilcea',146),('Pitesti',138)],
    'Pitesti': [('Rimnicu Vilcea',97),('Craiova',138),('Bucharest',101)],
    'Bucharest': [('Fagaras',211),('Pitesti',101),('Giurgiu',90),('Urziceni',85)],
    'Giurgiu': [('Bucharest',90)],
    'Urziceni': [('Bucharest',85),('Hirsova',98),('Vaslui',142)],
    'Hirsova': [('Urziceni',98),('Eforie',86)],
    'Eforie': [('Hirsova',86)],
    'Vaslui': [('Urziceni',142),('Iasi',92)],
    'Iasi': [('Vaslui',92),('Neamt',87)],
    'Neamt': [('Iasi',87)]
}

# heuristics (straight line distance to Bucharest) from your table
HEUR = {
 'Arad':366,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,'Fagaras':176,
 'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,'Mehadia':241,'Neamt':234,
 'Oradea':380,'Pitesti':100,'Rimnicu Vilcea':193,'Sibiu':253,'Timisoara':329,
 'Urziceni':80,'Vaslui':199,'Zerind':374
}

def a_star(start, goal):
    open_heap = []
    heapq.heappush(open_heap, (HEUR[start], start))
    came_from = {}
    gscore = {start: 0}
    fscore = {start: HEUR[start]}

    closed = set()

    while open_heap:
        f, current = heapq.heappop(open_heap)
        # goal?
        if current == goal:
            # reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, gscore[goal]

        closed.add(current)

        for neighbor, cost in GRAPH.get(current, []):
            tentative_g = gscore[current] + cost
            if neighbor in closed and tentative_g >= gscore.get(neighbor, inf):
                continue
            if tentative_g < gscore.get(neighbor, inf):
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g
                f = tentative_g + HEUR.get(neighbor, inf)
                fscore[neighbor] = f
                heapq.heappush(open_heap, (f, neighbor))
    return None, None

if __name__ == "__main__":
    path, cost = a_star("Arad","Bucharest")
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
