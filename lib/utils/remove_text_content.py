from bs4 import BeautifulSoup, NavigableString

def remove_text_content(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    
    # Function to remove text nodes
    def remove_text_nodes(tag):
        for content in tag.children:
            if isinstance(content, NavigableString):
                content.extract()

    # Apply the function to each tag in the parsed HTML
    for tag in soup.find_all(True):
        remove_text_nodes(tag)

    return str(soup)