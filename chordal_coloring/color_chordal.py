from is_chordal.is_chordal import all_previous_vertex_neighbours
from lex_bfs.lex_bfs import lex_bfs


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()              # zbiór sąsiadów

    def connect_to(self, v):
        self.out.add(v)


def color_chordal(graph):
    perfect_elimination_order = lex_bfs(graph)

    colors_quantity = 1
    vertex_color_list = [None] + [0 for _ in range(len(graph) - 1)]
    for i in range(1, len(perfect_elimination_order)):
        vertex_previous_neighbours = all_previous_vertex_neighbours(i, perfect_elimination_order, graph)
        used_colors = {vertex_color_list[neighbour] for neighbour in vertex_previous_neighbours}
        vertex_color, colors_quantity = get_lowest_unused_color(colors_quantity, used_colors)
        vertex_color_list[perfect_elimination_order[i]] = vertex_color

    return colors_quantity


def get_lowest_unused_color(colors_quantity, used_colors):
    for i in range(colors_quantity):
        if i not in used_colors:
            return i, colors_quantity
    return colors_quantity, colors_quantity + 1