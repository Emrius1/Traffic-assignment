import matplotlib.pyplot as plt
import networkx as nx


def plot_network(G, edge_flow=None, path=None, title="Road Network"):
    """
    返回 matplotlib Figure，供 Streamlit 显式渲染
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    pos = {node: (data["x"], data["y"]) for node, data in G.nodes(data=True)}

    nx.draw_networkx_nodes(
        G, pos,
        node_size=500,
        node_color="skyblue",
        ax=ax
    )
    nx.draw_networkx_labels(
        G, pos,
        font_size=12,
        font_weight="bold",
        ax=ax
    )

    nx.draw_networkx_edges(
        G, pos,
        width=2,
        edge_color="lightgray",
        arrows=True,
        ax=ax
    )

    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(
            G, pos,
            edgelist=path_edges,
            width=4,
            edge_color="red",
            arrows=True,
            ax=ax
        )

    if edge_flow:
        edge_labels = {
            (u, v): int(edge_flow.get((u, v), 0))
            for u, v in G.edges()
        }
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels,
            font_color="blue",
            ax=ax
        )

    ax.set_title(title)
    ax.axis("off")
    fig.tight_layout()

    return fig




if __name__ == "__main__":
    # 测试用例
    G = nx.DiGraph()
    G.add_node("A", x=0, y=0)
    G.add_node("B", x=1, y=1)
    G.add_edge("A", "B", length=1, t0=1, capacity=1800, q=0)
    plot_network(G, title="Test Network")
