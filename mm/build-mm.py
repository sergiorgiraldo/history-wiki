import os
import re
import graphviz
import shutil

def extract_links(folder):
    links = set()  # some files have duplicate links

    with open(folder, "r", encoding="utf-8") as file:
        content = file.read()
        
        regex = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)") # markdown links: [text](url), ignore image links
        matches = regex.findall(content)

        for match in matches:
            links.add(match[1])  # Extract the URL part 

    return links

def build_mindmap(folder):
    map = graphviz.Digraph(comment="Markdown Mind Map")

    for filename in os.listdir(folder):
        if filename.endswith(".md"):
            file_path = os.path.join(folder, filename)
            node_name = os.path.splitext(filename)[0]
            map.node(node_name, node_name) 
            
            links = extract_links(file_path)

            for link in links:
                link_name = os.path.splitext(os.path.basename(link))[0]
                map.edge(node_name, link_name)

    map.render("mindmap", format="png", cleanup=True)

    source = "mindmap.png"
    destination = "../docs/images/"
    shutil.move(source, os.path.join(destination, source))

if __name__ == "__main__":
    folder = "/Users/GK47LX/source/history-wiki/docs"
    build_mindmap(folder)
