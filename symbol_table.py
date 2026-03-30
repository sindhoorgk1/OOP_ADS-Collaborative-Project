class SymbolTable:
    """
    Bi-directional mapping between string URLs and integer IDs.
    """
    def __init__(self):
        self._url_to_id = {}
        self._id_to_url = {}
        self._next_id = 0

    def add(self, url: str) -> None:
        """Adds a URL to the symbol table if it doesn't already exist."""
        if url not in self._url_to_id:
            self._url_to_id[url] = self._next_id
            self._id_to_url[self._next_id] = url
            self._next_id += 1

    def contains(self, url: str) -> bool:
        """Checks if a URL is in the symbol table."""
        return url in self._url_to_id

    def index(self, url: str) -> int:
        """Returns the integer ID associated with the URL."""
        if url not in self._url_to_id:
            raise KeyError(f"URL {url} not found in symbol table.")
        return self._url_to_id[url]

    def name(self, index: int) -> str:
        """Returns the URL associated with the integer ID."""
        if index not in self._id_to_url:
            raise KeyError(f"Index {index} not found in symbol table.")
        return self._id_to_url[index]

    def size(self) -> int:
        """Returns the number of unique URLs in the symbol table."""
        return len(self._url_to_id)
