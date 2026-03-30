from mock_web_generator import create_mock_web
from crawler import WebCrawler
from pagerank import PageRank

def main():
    directory = 'mock_web'
    
    print("--- 1. Generating Mock Local Web ---")
    create_mock_web(directory)
    print("\n")

    print(f"--- 2. Crawling the Web (Starting from index.html) ---")
    crawler = WebCrawler(directory)
    # The starting point
    symbol_table, graph = crawler.crawl('index.html')

    print(f"Discovered {symbol_table.size()} pages.")
    print(f"Graph Structure: {graph.V()} Vertices, {graph.E()} Edges")
    print(graph)
    print("\n")

    print("--- 3. Calculating PageRank ---")
    pr = PageRank(graph)
    pr.compute()

    print("\n--- 4. Search Engine Results (Sorted by Authority/PageRank) ---")
    
    # Associate URL with Rank
    results = []
    for v in range(graph.V()):
        url = symbol_table.name(v)
        rank = pr.rank(v)
        results.append((url, rank))
        
    # Sort descending by rank
    results.sort(key=lambda x: x[1], reverse=True)

    print(f"{'URL':<25} | {'PageRank Score':<15}")
    print("-" * 45)
    for url, rank in results:
        print(f"{url:<25} | {rank:.6f}")

if __name__ == '__main__':
    main()
