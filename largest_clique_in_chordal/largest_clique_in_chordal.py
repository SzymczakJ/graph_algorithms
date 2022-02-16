from os import listdir
from os.path import isfile, join

from dimacs import loadWeightedGraph, readSolution
from is_chordal.is_chordal import all_previous_vertex_neighbours
from lex_bfs.lex_bfs import lex_bfs


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()

    def connect_to(self, v):
        self.out.add(v)


def largest_clique_in_chordal(graph):
    perfect_elimination_order = lex_bfs(graph)

    maximal_clique_size = 1
    for i in range(2, len(perfect_elimination_order)):
        all_prevoius_neighbours = all_previous_vertex_neighbours(i, perfect_elimination_order, graph)
        maximal_clique_size = max(len(all_prevoius_neighbours) + 1, maximal_clique_size)

    return maximal_clique_size