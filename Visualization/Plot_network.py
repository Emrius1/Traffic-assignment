
import matplotlib.pyplot as plt
import networkx as nx


def plot_network(
    G,
    edge_flow=None,
    path=None,
    label_mode="static",
    title="Road Network"
):
    fig, ax = plt.subplots(figsize=(8, 6))

    pos = {n: (d["x"], d["y"]) for n, d in G.nodes(data=True)}

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="skyblue", ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold", ax=ax)

    # base edges
    nx.draw_networkx_edges(
        G, pos,
        width=2,
        edge_color="lightgray",
        arrows=True,
        ax=ax
    )

    # highlight path
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

    # edge labels
    edge_labels = {}
    for u, v, data in G.edges(data=True):
        if label_mode == "static":
            edge_labels[(u, v)] = (
                f"C={data.get('capacity')}\n"
                f"V={data.get('speedmax')}"
            )
        elif label_mode == "flow" and edge_flow:
            edge_labels[(u, v)] = f"q={int(edge_flow.get((u, v), 0))}"
        elif label_mode == "time":
            edge_labels[(u, v)] = f"t={data.get('t0', 0):.2f}"

    if edge_labels:
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels,
            font_color="blue",
            font_size=9,
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
