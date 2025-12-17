from Tools.Graph_builder import build_graph
from Visualization.Plot_network import plot_network

def main():
    G = build_graph()

    plot_network(G, title="Road Network - Initial Flow")

if __name__ == "__main__":
    main()