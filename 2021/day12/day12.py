import networkx as nx

# Open data structure
with open ('day12/input.txt') as file:
    edges_list = [tuple(line.strip().split('-')) for line in file.readlines()]

# Make a graph out of the input
graph = nx.Graph()
graph.add_edges_from(edges_list)

# Draw graph for visibility/explainability
nx.draw(graph, with_labels=True, font_weight='bold')

class Path:
    """ Path travelled from starting point to location"""
    def __init__(self, starting_point, target, path, visited, small_cave_visited_twice):
        self.location = starting_point
        self.target = target
        self.path = path
        self.visited = visited
        self.visited_twice = small_cave_visited_twice

    def update_path(self, graph, paths, outcomes):

        if self.location == self.target:
            return paths, outcomes
        neighbours = list(nx.neighbors(graph, self.location))
        for neighbour in neighbours:
            if neighbour == self.target:
                outcomes.append(self.path + [neighbour])
            if (neighbour not in self.visited or neighbour[0].isupper()) or (not self.visited_twice and neighbour != 'start'):
                if neighbour in self.visited and neighbour[0].islower() or self.visited_twice:
                    visited_twice = True
                else:
                    visited_twice = False
                new_path = Path(neighbour, self.target, self.path + [neighbour], self.visited + [neighbour], visited_twice)
                paths.append(new_path)
        return paths, outcomes


routes = [Path('start', 'end', ['start'], ['start'], False)]
outcomes = []

for path in routes:
    test, outcomes = path.update_path(graph, routes, outcomes)

outcomes = sorted(outcomes)
print(len(outcomes))
