import os
import re
import graphviz
import shutil

def extract_links(file_path):
    """Extract links from a markdown file."""
    links = set()  # some files have duplicate links
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        # Find markdown links [text](url)
        link_pattern = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")
        matches = link_pattern.findall(content)
        for match in matches:
            links.add(match[1])  # Extract the URL part and add to the set
    return links

def build_mindmap(directory):
    dot = graphviz.Digraph(comment="Markdown Mind Map")

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            node_name = os.path.splitext(filename)[0]
            dot.node(node_name, node_name) 
            links = extract_links(file_path)
            for link in links:
                link_name = os.path.splitext(os.path.basename(link))[0]
                dot.edge(node_name, link_name)

    dot.render("mindmap", format="png", cleanup=True)

    source = "mindmap.png"
    destination = "../docs/"
    shutil.move(source, os.path.join(destination, source))

if __name__ == "__main__":
    directory = "/Users/GK47LX/source/history-wiki/docs"
    build_mindmap(directory)
