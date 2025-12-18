import networkx as nx


def shortest_path_freeflow(G, origin, destination):
    """
    自由流最短路径（不考虑拥堵）
    使用 t0 作为边权重
    """
    path = nx.shortest_path(
        G,
        source=origin,
        target=destination,
        weight="t0"
    )

    travel_time = nx.shortest_path_length(
        G,
        source=origin,
        target=destination,
        weight="t0"
    )

    return path, travel_time