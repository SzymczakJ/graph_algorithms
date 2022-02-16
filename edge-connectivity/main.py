from queue import PriorityQueue


class Node:
  def __init__(self):
    self.edges = {}
    self.merged_with = []

  def addEdge( self, to, weight):
    self.edges[to] = self.edges.get(to,0) + weight


  def notifyOfMerging(self, vertex):
    self.merged_with.append(vertex)

  def delEdge( self, to ):
    del self.edges[to]

  def printEdges(self):
    print(self.edges)

def merge_vertices( G, x, y):
  for vertex in G[y].edges:
    if vertex != x:
      G[x].addEdge(vertex, G[y].edges[vertex])
  G[x].notifyOfMerging(y)

  for i in range(len(G)):
    if y in G[i].edges:
      if not i == y and not i == x:
        G[i].addEdge(x, G[i].edges[y])
      G[i].delEdge(y)

  G[y].edges.clear()

def minimumCut(G, merged_vertices_number):
  queue = PriorityQueue()
  checked_list = [0]
  visited = [False for _ in range(len(G))]
  visited[0] = True

  for vertex in G[0].edges:
    queue.put((-G[0].edges[vertex], vertex))

  while len(checked_list) - merged_vertices_number < len(G) and not queue.empty():
    _, vertex = queue.get()
    if not visited[vertex]:
      visited[vertex] = True
      checked_list.append(vertex)
      for next_vertex in G[vertex].edges:
        if not visited[next_vertex]:
          update_priority_queue(G, next_vertex, visited, queue)

  possible_minimal_cut = 0
  for vertex in G[checked_list[-1]].edges:
    possible_minimal_cut += G[checked_list[-1]].edges[vertex]

  merge_vertices(G, checked_list[-1], checked_list[-2])

  return possible_minimal_cut

def stoer_wagner_algorithm(G):
  res = float('inf')
  for i in range(len(G) - 1):
    res = min(res, minimumCut(G, i))

  return res

def update_priority_queue(G, x, visited, priority_queue):
  connection_weight = 0
  for vertex in G[x].edges:
    if visited[vertex]:
      connection_weight += G[x].edges[vertex]

  priority_queue.put((-connection_weight, x))


def print_graph(G):
  for vertex in G:
    vertex.printEdges()
  print()
