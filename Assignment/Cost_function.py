def travel_time(edge_data, consider_congestion=False):

    t0 = edge_data["t0"]

    if not consider_congestion:
        return t0

    q = edge_data.get("q", 0)
    cap = edge_data["capacity"]

    return t0 * (1 + (q / cap) ** 2)