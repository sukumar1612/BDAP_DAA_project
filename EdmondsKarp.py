from copy import deepcopy


class EdmondsKarp:
    def __init__(self, input_matrix):
        self.graph = deepcopy(input_matrix)
        self.count = 0
        self.row_count = len(input_matrix)

    def edmonds_karps_algorithm(self, source, sink):
        parent = [-1] * self.row_count
        paths = []
        max_flow = 0
        while self.breadth_first_search(source, sink, parent):
            path_flow = 1000000000
            s = sink
            path = []
            self.count = self.count + 1
            while s != source:
                path.append(s)
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            paths.append(path)
            max_flow += path_flow
            v = sink
            while v != source:
                self.count = self.count + 1
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow, paths, self.count

    def breadth_first_search(self, s, t, parent):
        visited = [False] * self.row_count
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] is False and val > 0:
                    self.count = self.count + 1
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False