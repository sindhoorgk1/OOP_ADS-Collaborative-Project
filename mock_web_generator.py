import os

def create_mock_web(directory: str):
    """Generates interconnected HTML pages to simulate a local web."""
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the pages and their outbound links
    pages_data = {
        'index.html': ['about.html', 'contact.html', 'products.html'],
        'about.html': ['index.html', 'team.html'],
        'contact.html': ['index.html'],
        'products.html': ['productA.html', 'productB.html', 'index.html'],
        'productA.html': ['products.html', 'checkout.html'],
        'productB.html': ['products.html', 'checkout.html'],
        'team.html': ['about.html'],
        'checkout.html': ['index.html'],  # checkout links back to home
        'dangling.html': [] # Example of a dangling node (no outbound links)
    }

    # Also add a link to a dangling page for testing
    pages_data['about.html'].append('dangling.html')

    for filename, links in pages_data.items():
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"<!DOCTYPE html>\n<html>\n<head><title>{filename}</title></head>\n<body>\n")
            f.write(f"<h1>Welcome to {filename}</h1>\n")
            f.write("<ul>\n")
            for link in links:
                f.write(f'  <li><a href="{link}">Go to {link}</a></li>\n')
            f.write("</ul>\n")
            f.write("</body>\n</html>\n")

    print(f"Mock web created in directory: {directory}")

if __name__ == '__main__':
    create_mock_web('mock_web')
