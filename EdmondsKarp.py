class EdmondsKarp:
    def __init__(self, input_matrix):
        self.graph = input_matrix
        self.ROW = len(input_matrix)

    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.ROW

        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        print(parent)
        return max_flow