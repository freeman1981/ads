class Vertex:
    def __init__(self, key: str):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr: 'Vertex', weight: int = 0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return f'{self.id} connected to: {[x.id for x in self.connected_to]}'

    @property
    def connections(self):
        return self.connected_to.keys()


class Graph:
    def __init__(self):
        self.verts = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        self.verts[key] = Vertex(key)

    def get_vertex(self, n):
        return self.verts.get(n)

    def __contains__(self, n):
        return n in self.verts

    def add_edge(self, f, t, cost=0):
        if f not in self.verts:
            self.add_vertex(f)
        if t not in self.verts:
            self.add_vertex(t)
        self.verts[f].add_neighbor(self.verts[t], cost)

    def get_vertices(self):
        return self.verts.keys()

    def __iter__(self):
        return iter(self.verts.values())

