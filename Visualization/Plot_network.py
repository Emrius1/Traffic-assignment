import matplotlib
# 固定后端，避免 PyCharm / 系统冲突
matplotlib.use("TkAgg")  # 或 "Qt5Agg"，TkAgg 通常自带

import matplotlib.pyplot as plt
import networkx as nx


def plot_network(G, edge_flow=None, title="Road Network"):
    """
    可视化路网
    G: NetworkX 图
    edge_flow: dict {(u,v): flow_value}，可选
    """
    # 节点位置
    pos = {node: (data["x"], data["y"]) for node, data in G.nodes(data=True)}

    plt.figure(figsize=(8, 6))

    # 画节点
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color="skyblue")
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

    # 画边
    if edge_flow:
        # 根据流量调整线宽
        widths = [edge_flow.get((u, v), 1) / 500 for u, v in G.edges()]  # 缩放
        nx.draw_networkx_edges(G, pos, width=widths, edge_color="orange", arrows=True)
        # 标注流量
        edge_labels = {(u, v): str(edge_flow.get((u, v), 0)) for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
    else:
        nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", arrows=True)

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 测试用例
    G = nx.DiGraph()
    G.add_node("A", x=0, y=0)
    G.add_node("B", x=1, y=1)
    G.add_edge("A", "B", length=1, t0=1, capacity=1800, q=0)
    plot_network(G, title="Test Network")
