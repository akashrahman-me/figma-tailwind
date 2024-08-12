from bs4 import BeautifulSoup

def extract_inline_css(html):
    # Create a BeautifulSoup instance
    soup = BeautifulSoup(html, "html.parser")

    # Initialize the result string
    result = ""

    # Traverse the DOM
    def traverse_dom(node):
        nonlocal result  # Python's way to access outer scope variable
        if node is not None and node.name is not None:  # Check if the node is not None and is Element
            style = node.get("style")
            if style is not None:
                # If the node has a 'style' attribute, add it to the result
                styles = style.split(";")
                for s in styles:
                    trimmed = s.strip()
                    if trimmed != "":
                        result += trimmed + ";\n"
                result += "\n"

            # Recurse for each child node
            for child in node.children:
                traverse_dom(child)

    # Start the traversal
    traverse_dom(soup.body)

    return result
