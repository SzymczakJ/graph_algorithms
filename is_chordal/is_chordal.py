from lex_bfs.lex_bfs import lex_bfs


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()

    def connect_to(self, v):
        self.out.add(v)


def is_chordal(graph):
    elimination_order = lex_bfs(graph)

    for i in range(2, len(elimination_order)):
        latest_neighbour_index = vertex_latest_neighbour_index(i, elimination_order, graph)
        vertex_neighbours = all_previous_vertex_neighbours(i, elimination_order, graph)
        latest_neighbour_neighbours = all_previous_vertex_neighbours(latest_neighbour_index, elimination_order, graph)
        if not vertex_neighbours - {elimination_order[latest_neighbour_index]} <= latest_neighbour_neighbours:
            return False

    return True


def vertex_latest_neighbour_index(vertex_index, elimination_order, graph):
    vertex = elimination_order[vertex_index]
    for i in range(vertex_index - 1, -1, -1):
        possible_neighbour = elimination_order[i]
        if possible_neighbour in graph[vertex].out:
            return i


def all_previous_vertex_neighbours(vertex_index, elimination_order, graph):
    vertex = elimination_order[vertex_index]
    previous_neighbours = set()
    for i in range(vertex_index - 1, -1, -1):
        possible_neighbour = elimination_order[i]
        if possible_neighbour in graph[vertex].out:
            previous_neighbours.add(possible_neighbour)
    return previous_neighbours