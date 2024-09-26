# Реализовать граф с направленными рёбрами

from collections import deque

class Graph:
    def __init__(self, num_nodes):
        self.nodes = num_nodes
        self.graph = {i: [] for i in range(self.nodes)}

    def add_edge(self, n1, n2):
        if n1 >= self.nodes or n2 >= self.nodes or n1 < 0 or n2 < 0:
            raise ValueError(f"Узлы должны быть в диапазоне от 0 до {self.nodes - 1}")
        self.graph[n1].append(n2)

    def print_graph(self):
        for node in self.graph:
            for neighbor in self.graph[node]:
                print(f"{node} -> {neighbor}")

    def bfs(self, start_node):
        visited = [False] * self.nodes
        queue = deque()
        visited[start_node] = True
        queue.append(start_node)
        while queue:
            s = queue.popleft()
            for neighbor in self.graph[s]:
                if not visited[neighbor]:
                    print(f"{s} -> {neighbor}")
                    visited[neighbor] = True
                    queue.append(neighbor)

    def dfs_util(self, node, visited):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                print(f"{node} -> {neighbor}")
                self.dfs_util(neighbor, visited)

    def dfs(self, start_node):
        visited = [False] * self.nodes
        self.dfs_util(start_node, visited)


# Пример использования
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)

print("Рёбра графа:")
g.print_graph()

print("\nОбход в ширину (BFS) начиная с узла 0:")
g.bfs(0)

print("\nОбход в глубину (DFS) начиная с узла 0:")
g.dfs(0)

