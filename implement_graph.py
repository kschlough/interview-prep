# implement a graph 2 ways from Joe James YT tutorial

# undirected graph using adjacency lists
class vertex:
    def __init__(self, n):
        self.name = n
        self.neighbours = list() # adjacency lists stored locally 

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

# undirected graph (weighted & unweighted edges) with adjacency matrix
class vertex:
    def __init__(self, n):
        self.name = n # name of the vertex
        # adjacency lists not stored locally, stored centrally in the graph

class graph:
    vertices = {}
    edges = [] # 2-d array of edges
    edge_indices = {} # so we can quickly locate index of any edge given name

    def add_vertex(self, vert):
        if isinstance(vert, vertex) and vert.name not in self.vertices:
            self.vertices[vert.name] = vert
            for row in self.edges:
                row.append(0) # add with all 0s because we haven't mapped any edges yet
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vert.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight = 1): # edges matrix is symmetrical across the diagonal
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end = ' ')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end = ' ')
            print(' ')

# testing implementation
g = graph()
a = vertex('A')
g.add_vertex(a)
g.add_vertex(vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()



