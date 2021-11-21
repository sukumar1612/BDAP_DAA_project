from copy import deepcopy
# import numpy as np


class FordFulkerson:
    def __init__(self, input_matrix):
        self.graph = deepcopy(input_matrix)
        self.ROW = len(input_matrix)
        self.count = 0

    def dfs(self, s, t, parent, visited):

        for ind, val in enumerate(self.graph[s]):
            self.count = self.count + 1
            if visited[ind] is False and val > 0:
                parent[ind] = s
                if ind != t:
                    visited[ind] = True
                    if self.dfs(ind, t, parent, visited):
                        return True
                else:
                    return True
        return False

    def ford_fulkerson(self, source, sink):

        paths = []
        max_flow = 0
        parent = [-1] * self.ROW
        visited = [False] * self.ROW
        visited[source] = True
        while True:
            path = []
            if self.dfs(source, sink, parent, visited):
                self.count = self.count + 1
                path_flow = float("Inf")
                t = sink
                path.append(t)
                while t != source:
                    self.count = self.count + 1
                    path_flow = min(path_flow, self.graph[parent[t]][t])
                    path.append(parent[t])
                    t = parent[t]
                paths.append(path)
                max_flow += path_flow
                v = sink
                while v != source:
                    self.count = self.count + 1
                    u = parent[v]
                    if self.graph[u][v]:
                        self.graph[u][v] -= path_flow
                    if self.graph[v][u]:
                        self.graph[v][u] -= path_flow
                    v = parent[v]
                for i in range(len(parent)):
                    parent[i] = -1
            else:
                break

        return max_flow, paths, self.count
