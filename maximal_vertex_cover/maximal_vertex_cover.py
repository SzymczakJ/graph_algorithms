from os import listdir
from os.path import isfile, join

from dimacs import loadWeightedGraph, readSolution
from lex_bfs.lex_bfs import lex_bfs


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()              # zbiór sąsiadów

    def connect_to(self, v):
        self.out.add(v)


def maximal_vertex_cover(graph):
    vertex_order = lex_bfs(graph)
    vertex_order = vertex_order[::-1]
    independent_set = set()

    for vertex in vertex_order:
        vertex_neighbours = get_all_neighbours(graph, vertex)
        if not vertex_neighbours & independent_set:
            independent_set.add(vertex)

    all_vertices = {i for i in range(1, len(graph))}

    return all_vertices - independent_set


def get_all_neighbours(graph, vertex):
    neighbours = set()
    for vertex in graph[vertex].out:
        neighbours.add(vertex)
    return neighbours
