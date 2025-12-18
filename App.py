# app.py
import streamlit as st

from Tools.Graph_builder import build_graph
from Assignment.Shortest_Path import (
    shortest_path_freeflow,
    shortest_path_congested
)
from Visualization.Plot_network import plot_network


st.set_page_config(
    page_title="Traffic Assignment Demo",
    layout="centered"
)

st.title("🚦 Traffic Assignment Demo")

# build network
G = build_graph()
nodes = list(G.nodes)

# selection
origin = st.selectbox("Origin", nodes)
destination = st.selectbox("Destination", nodes)

mode = st.radio(
    "Travel Time Model",
    ["Free-flow", "Congested (BPR)"]
)

if st.button("Find Shortest Path"):
    if mode == "Free-flow":
        path, tt = shortest_path_freeflow(G, origin, destination)
        title = "Free-flow Shortest Path"
    else:
        path, tt = shortest_path_congested(G, origin, destination)
        title = "Congested Shortest Path (BPR)"

    st.markdown(f"**Path:** {' → '.join(path)}")
    st.markdown(f"**Travel time:** {tt:.3f}")

    fig = plot_network(
        G,
        path=path,
        label_mode="static",
        title=title
    )
    st.pyplot(fig)