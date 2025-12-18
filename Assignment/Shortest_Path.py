# Assignment/shortest_path.py
import networkx as nx


def shortest_path_freeflow(G, origin, destination):
    """
    自由流最短路（不考虑拥堵）
    """
    path = nx.shortest_path(G, origin, destination, weight="t0")
    tt = nx.shortest_path_length(G, origin, destination, weight="t0")
    return path, tt


def shortest_path_congested(G, origin, destination, alpha=0.15, beta=4):
    """
    考虑拥堵的最短路（BPR）
    t = t0 * (1 + alpha * (q / c)^beta)
    """

    def travel_time(u, v, data):
        q = data.get("q", 0)
        c = data.get("capacity", 1)
        t0 = data.get("t0", 1.0)
        return t0 * (1 + alpha * (q / c) ** beta)

    path = nx.shortest_path(
        G,
        origin,
        destination,
        weight=travel_time
    )

    tt = 0.0
    for u, v in zip(path[:-1], path[1:]):
        tt += travel_time(u, v, G[u][v])

    return path, tt
