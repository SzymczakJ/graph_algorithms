class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()              # zbiór sąsiadów

    def connect_to(self, v):
        self.out.add(v)


def lex_bfs(graph):
    lex_order = [1]
    lex_unvisited_list = []
    first_vertex_neighbours = set()
    others = set()
    for i in range(2, len(graph)):
        if i in graph[1].out:
            first_vertex_neighbours.add(i)
        else:
            others.add(i)
    if others:
        lex_unvisited_list.append(others)
    if first_vertex_neighbours:
        lex_unvisited_list.append(first_vertex_neighbours)

    while lex_unvisited_list:
        vertex = lex_unvisited_list[-1].pop()
        lex_order.append(vertex)
        if not lex_unvisited_list[-1]:
            lex_unvisited_list.pop(-1)

        new_lex_unvisited_list = []
        for i in range(len(lex_unvisited_list)):
            vertex_neigbours = set()
            others = set()
            while lex_unvisited_list[i]:
                unvisited_vertex = lex_unvisited_list[i].pop()
                if unvisited_vertex in graph[vertex].out:
                    vertex_neigbours.add(unvisited_vertex)
                else:
                    others.add(unvisited_vertex)
            if others:
                new_lex_unvisited_list.append(others)
            if vertex_neigbours:
                new_lex_unvisited_list.append(vertex_neigbours)
        lex_unvisited_list = new_lex_unvisited_list
    return lex_order
