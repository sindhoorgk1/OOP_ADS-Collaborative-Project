class Digraph:
    """
    A directed graph representation using adjacency lists.
    """
    def __init__(self, V: int = 0):
        self._V = V
        self._E = 0
        # Initialize an empty list of adjacent vertices for each vertex
        self._adj = {v: [] for v in range(V)}

    def add_vertex(self) -> int:
        """Adds a new vertex to the graph and returns its ID."""
        v = self._V
        self._adj[v] = []
        self._V += 1
        return v

    def add_edge(self, v: int, w: int) -> None:
        """Adds a directed edge v -> w to the graph."""
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._adj[v].append(w)
        self._E += 1

    def adj(self, v: int) -> list:
        """Returns the list of vertices adjacent from vertex v."""
        self._validate_vertex(v)
        return self._adj[v]

    def V(self) -> int:
        """Returns the number of vertices in this digraph."""
        return self._V

    def E(self) -> int:
        """Returns the number of edges in this digraph."""
        return self._E

    def out_degree(self, v: int) -> int:
        """Returns the number of outgoing directed edges from vertex v."""
        self._validate_vertex(v)
        return len(self._adj[v])

    def _validate_vertex(self, v: int) -> None:
        if v < 0 or v >= self._V:
            raise ValueError(f"Vertex {v} is not between 0 and {self._V - 1}")

    def __str__(self) -> str:
        s = f"{self._V} vertices, {self._E} edges\n"
        for v in range(self._V):
            s += f"{v}: "
            for w in self._adj[v]:
                s += f"{w} "
            s += "\n"
        return s
