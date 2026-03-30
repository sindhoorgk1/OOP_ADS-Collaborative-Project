from digraph import Digraph

class PageRank:
    """
    Calculates PageRank scores for nodes in a Digraph using Power Iteration.
    """
    def __init__(self, graph: Digraph, alpha: float = 0.85, epsilon: float = 1e-6, max_iterations: int = 100):
        self._graph = graph
        self._alpha = alpha
        self._epsilon = epsilon
        self._max_iterations = max_iterations
        self._V = self._graph.V()
        # Initialize Uniform rank distribution
        if self._V == 0:
            self._ranks = []
        else:
            self._ranks = [1.0 / self._V] * self._V

    def compute(self) -> None:
        """
        Performs the power iteration step to calculate PageRanks.
        """
        if self._V == 0:
            return

        out_degrees = [self._graph.out_degree(v) for v in range(self._V)]
        
        for iteration in range(self._max_iterations):
            new_ranks = [0.0] * self._V
            dangling_rank_sum = 0.0

            # 1. Distribute ranks from vertices
            for v in range(self._V):
                deg = out_degrees[v]
                if deg > 0:
                    prob = 1.0 / deg
                    # Distribute equally to all outward nodes
                    for w in self._graph.adj(v):
                        new_ranks[w] += self._ranks[v] * prob
                else:
                    # Dangling node: acts as if it links to all nodes in the graph
                    dangling_rank_sum += self._ranks[v]

            # 2. Add teleportation factor + distribute dangling node mass
            diff = 0.0
            for v in range(self._V):
                # Apply damping factor (alpha)
                new_ranks[v] = self._alpha * new_ranks[v]
                
                # Distribute dangling node rank uniformly
                new_ranks[v] += self._alpha * (dangling_rank_sum / self._V)
                
                # Teleportation: 1 - alpha probability of jumping to ANY random page
                new_ranks[v] += (1.0 - self._alpha) / self._V

                # Calculate convergence diff
                diff += abs(new_ranks[v] - self._ranks[v])

            self._ranks = new_ranks

            # 3. Check for convergence
            if diff < self._epsilon:
                print(f"Converged after {iteration + 1} iterations.")
                break
        else:
            print(f"Warning: Did not converge after {self._max_iterations} iterations.")

    def rank(self, v: int) -> float:
        """Returns the computed PageRank for a specific vertex."""
        if v < 0 or v >= self._V:
            raise ValueError("Invalid vertex.")
        return self._ranks[v]

    def all_ranks(self) -> list:
        """Returns the full list of PageRanks."""
        return self._ranks.copy()
