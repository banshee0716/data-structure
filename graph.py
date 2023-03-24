class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            visited.add(vertex)
            print("DFS遍歷節點：", list(visited))
            for neighbor in self.adj_list[vertex]:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set([start_vertex])
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            print("BFS遍歷節點：", list(visited))
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
# 建立一個簡單的圖形
graph = Graph()
for v in ["A", "B", "C", "D", "E", "F"]:
    graph.add_vertex(v)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")

print("DFS traversal:")
graph.dfs("A")
print()

print("BFS traversal:")
graph.bfs("A")
print()
