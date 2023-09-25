import heapq


class Grafo:
    def __init__(self):
        self.grafo = {}

    def adiciona_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adiciona_aresta(self, vertice1, vertice2, peso):
        self.adiciona_vertice(vertice1)
        self.adiciona_vertice(vertice2)
        self.grafo[vertice1].append((vertice2, peso))
        self.grafo[vertice2].append((vertice1, peso))

    def grau(self, vertice):
        return len(self.grafo[vertice])

    def grau_grafo(self):
        return sum([self.grau(v) for v in self.grafo]) // 2

    def dijkstra(self, inicio):
        dist = {v: float('inf') for v in self.grafo}
        dist[inicio] = 0
        pq = [(0, inicio)]

        while pq:
            _, v = heapq.heappop(pq)

            for vizinho, peso in self.grafo[v]:
                alt = dist[v] + peso
                if alt < dist[vizinho]:
                    dist[vizinho] = alt
                    heapq.heappush(pq, (alt, vizinho))

        return dist


# Exemplo de uso
g = Grafo()
g.adiciona_aresta('A', 'B', 1)
g.adiciona_aresta('A', 'C', 3)
g.adiciona_aresta('B', 'D', 2)
g.adiciona_aresta('C', 'D', 1)
print(g.dijkstra('A'))
print(g.grau('A'))  # 2
print(g.grau_grafo())  # 4
