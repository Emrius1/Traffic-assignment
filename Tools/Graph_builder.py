import networkx as nx
from Tools.Network_reader import read_network
import math

def build_graph():
    nodes, links = read_network()
    G = nx.DiGraph()

    for name, x, y in zip(nodes["name"], nodes["x"], nodes["y"]):
        G.add_node(name, x=x, y=y)

    for i, link_name in enumerate(links["between"]):
        u, v = link_name[0], link_name[1]
        capacity = links["capacity"][i]
        speedmax = links["speedmax"][i]

        x1, y1 = G.nodes[u]["x"], G.nodes[u]["y"]
        x2, y2 = G.nodes[v]["x"], G.nodes[v]["y"]

        length = math.hypot(x2 - x1, y2 - y1)

        t0 = length / speedmax

        G.add_edge(
            u, v,
            length=length,
            t0=t0,
            capacity=capacity,
            speedmax=speedmax,
            q=0
        )

        G.add_edge(
            v, u,
            length=length,
            t0=t0,
            capacity=capacity,
            speedmax=speedmax,
            q=0
        )

    return G
