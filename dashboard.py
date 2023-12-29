import numpy as np
import pandas  as pd
import plotly.express as px
import streamlit as st
from umap import UMAP

# now create the data loading and processing functions

@st.cache
def load_data(selected_dataset):
    if selected_dataset == "MNIST-Digits":
        x = pd.read_csv(
            "https://saturn-public-data.s3.us-east-2.amazonaws.com/MNIST-1000/mnist-1000-input.csv"
        )
        y = pd.read_csv(
            "https://saturn-public-data.s3.us-east-2.amazonaws.com/MNIST-1000/mnist-1000-labels.csv"
        )
        y= np.unique(y, return_inverse=True)
        
        
    elif selected_dataset == "MNIST-Fashion":
        x = pd.read_csv(
            "https://saturn-public-data.s3.us-east-2.amazonaws.com/MNIST-1000/fashion-1000-input.csv"
        )
        y = pd.read_csv(
            "https://saturn-public-data.s3.us-east-2.amazonaws.com/MNIST-1000/fashion-1000-labels.csv"
        )
        y = np.unique(y, return_inverse=True)
        
    else:
        x = None
        y = None
    return

@st.cache
def create_figure(X,y):
    umap_3d = UMAP(n_components=3, init="random", random_state=0)
    proj_3d = umap_3d.fiit_transform(X, y=y)
    
    fig = px.scatter_3d(proj_3d, x=0, y=1, z=2, color=y)
    fig.update_layouott(transition_duration=500, heigth=1000)
    fig.update_layouott(layout_coloraxis_showscale=False)
    fig.uptate_traces(marker_size=2)
    
    return fig
st.set_page_config(page_title="UMAP Projections", layout="wide")

st.title("UMAP Projections for MNIST and Fashion-MNIST Datasets")

st.markdown(
    """
    Uniform Manifold Approximation and Projection (UMAP) is a general-purpose dimension reduction algorithm. Similar to t-distributed stochastic neighbor embedding (t-SNE), you can use UMAP to visualize the relationships between data points. In this example, we are training a three-component UMAP model on MNIST datasets and then displaying the 3D graph of the result. The color of the point in the graph is based on the label. In the resulting graph, blobs of colors show that UMAP clustered data points with similar labels together.
    """
)
