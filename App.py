import streamlit as st
from Tools.Graph_builder import build_graph
from Assignment.Shortest_Path import shortest_path_freeflow
from Visualization.Plot_network import plot_network

st.set_page_config(page_title="Traffic Assignment Demo", layout="centered")

st.title("🚦 Traffic Assignment Software")

G = build_graph()

nodes = list(G.nodes)

origin = st.selectbox("Origin", nodes)
destination = st.selectbox("Destination", nodes)

if st.button("Find Free-flow Shortest Path"):
    path, tt = shortest_path_freeflow(G, origin, destination)
    st.write("**Path:**", " → ".join(path))
    st.write("**Free-flow travel time:**", round(tt, 3))

    plot_network(G, path=path, title="Free-flow Shortest Path")
    st.pyplot()
