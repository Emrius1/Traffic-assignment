import json

def read_network(file_path="Data/Network.json"):
    with open(file_path, "r") as f:
        data = json.load(f)
    nodes = data["nodes"]
    links = data["links"]
    return nodes, links
