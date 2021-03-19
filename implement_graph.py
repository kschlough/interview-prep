# implement a graph 2 ways from Joe James YT tutorial

# undirected graph using adjacency lists
class vertex:
    def __init__(self, n):
        self.name = n
        self.neighbours = list()

    def add_neighbours(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

class graph:
    vertices = {} # dictionary of vertices so we can find any vertex by its name

    def add_vertex(self, vert):
        if isinstance(vert, vertex) and vert.name not in self.vertices: # check it's a vertex object and not in dict
            self.vertices[vert.name] = vert
            return True
        else:
            return False

    def add_edge(self, u, v): # add edge w/ vertices u & v
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbour(v)
                if key == v:
                    value.add_neighbour(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours))

# testing implementation
g = graph()
a = vertex('a')
g.add_vertex(a)
g.add_vertex(vertex('b'))
for i in range(ord('a'), ord('k')):
    g.add_vertex(vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()

# adjacency matrix