import os
import re
from symbol_table import SymbolTable
from digraph import Digraph

class WebCrawler:
    """
    Simulates a web crawler traversing local HTML files to build a web graph.
    """
    def __init__(self, start_directory: str):
        self.directory = start_directory
        self.symbol_table = SymbolTable()
        self.graph = Digraph(0)
        # Using a simple queue for BFS traversal
        self._queue = []
        self._visited = set()

    def _extract_links(self, html_content: str) -> list:
        """Extracts href values from anchor tags using a simple regex."""
        # Simple regex to find href="something"
        # Not perfect for real HTML, but sufficient for simulation
        pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
        matches = re.findall(pattern, html_content)
        return matches

    def crawl(self, start_file: str) -> tuple:
        """
        Crawls the local mock web starting from a seed file.
        Returns the populated SymbolTable and Digraph.
        """
        seed_path = os.path.join(self.directory, start_file)
        if not os.path.exists(seed_path):
            raise FileNotFoundError(f"Starting point not found: {seed_path}")

        # Add start node to symbol table and graph
        self.symbol_table.add(start_file)
        self.graph.add_vertex()
        
        self._queue.append(start_file)

        while self._queue:
            current_url = self._queue.pop(0)

            if current_url in self._visited:
                continue
            
            self._visited.add(current_url)

            current_id = self.symbol_table.index(current_url)
            filepath = os.path.join(self.directory, current_url)

            # If the file exists, read its content and find outer links
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                links = self._extract_links(content)
                for target_url in links:
                    # Resolve relative URLs if necessary (assuming all in same folder for simplicity)
                    target_url = target_url.split('#')[0] # Ignore fragments
                    
                    if not target_url:
                        continue

                    # If URL unseen, add to ST and Graph
                    if not self.symbol_table.contains(target_url):
                        self.symbol_table.add(target_url)
                        self.graph.add_vertex()
                        self._queue.append(target_url)
                    
                    target_id = self.symbol_table.index(target_url)
                    
                    # Add directed edge from current URL to target URL
                    self.graph.add_edge(current_id, target_id)
            else:
                print(f"Warning: Crawler hit a dead link - {current_url}")

        return self.symbol_table, self.graph
