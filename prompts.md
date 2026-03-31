## File1 Crawler.py
Create a Python class called WebCrawler that simulates crawling local HTML files in a directory. It should initialize with a directory path and maintain a graph structure.
Extend the WebCrawler class to include:
- A SymbolTable to map URLs to indices
- A Digraph to represent links
- A queue for BFS traversal
- A visited set
Write a Python function that extracts all href links from HTML content using regex. Keep it simple and assume well-formed HTML.
Implement a crawl method that:
- Starts from a given HTML file
- Uses BFS traversal
- Reads file content
- Extracts links
- Builds a directed graph
Modify the crawler to:
- Use os.path to resolve file paths
- Raise FileNotFoundError if the start file doesn't exist
- Print a warning for dead links
Update the crawler so that:
- Each new URL is added to the SymbolTable
- A new vertex is added to the graph
- Directed edges are added between pages
Modify the crawl method to return both the SymbolTable and the Digraph.

## File2 pagerank.py

Create a Python class PageRank that computes PageRank for a directed graph using power iteration.
Initialize the PageRank class with:
- A Digraph
- Damping factor (alpha)
- Convergence threshold (epsilon)
- Max iterations

Also initialize ranks uniformly.
Implement the PageRank algorithm using power iteration:
- Distribute rank across outgoing edges
- Handle dangling nodes
- Apply damping factor
Modify the PageRank algorithm to handle dangling nodes (nodes with no outgoing edges) by redistributing their rank evenly.
Add teleportation to the PageRank algorithm using (1 - alpha) / N.
Add a convergence check using epsilon and stop iterations when the difference between ranks is small.
Add a maximum iteration limit and print a warning if convergence is not reached.
Add methods:
- rank(v): return rank of a node
- all_ranks(): return all PageRank values