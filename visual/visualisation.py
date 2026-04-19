# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module visualisation : lance la chaîne visuelle

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# from mpl_toolkits.mplot3d import Axes3D  # sera utilisé pour la 3D plus tard


# ---------------------------------------------------------
# 1) VISUALISATION : Hiérarchie verticale
# ---------------------------------------------------------
def plot_vertical(t_ordre):
    fig, ax = plt.subplots(figsize=(6, 14))

    def on_key(event):
        if getattr(event, "key", None) == "escape":
            plt.close(event.canvas.figure)

    fig.canvas.mpl_connect('key_press_event', on_key)

    for level, tetra in t_ordre.items():
        ax.scatter(0, -level, s=200, color="skyblue", edgecolor="black")
        ax.text(0.1, -level, tetra, fontsize=10, va="center")
    ax.set_title("Hiérarchie tétracordique")
    ax.set_axis_off()

    plt.show()

    return fig


# ---------------------------------------------------------
# 2) VISUALISATION : Constellation circulaire
# ---------------------------------------------------------
def plot_constellation(t_ordre):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect("equal")

    max_level = max(t_ordre.keys())

    for level, tetra in t_ordre.items():
        angle = 2 * np.pi * (level / max_level)
        radius = level * 0.3
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        ax.scatter(x, y, s=200, color="orange", edgecolor="black")
        ax.text(x, y, tetra, fontsize=8, ha="center", va="center")

    ax.set_title("Constellation tétracordique")
    ax.set_axis_off()
    return fig


# ---------------------------------------------------------
# 3) VISUALISATION : NetworkX 3D
# ---------------------------------------------------------
def plot_network_3d(t_ordre, relations):
    ndg = nx.DiGraph()

    for level, tetra in t_ordre.items():
        ndg.add_node(tetra, level=level)

    for src, data in relations["juxta"].items():
        if isinstance(data, tuple):
            dst = data[3]
            if src in ndg and dst in ndg:
                ndg.add_edge(src, dst)

    pos = nx.spring_layout(ndg, dim=3, seed=42)

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")

    xs = [pos[n][0] for n in ndg.nodes()]
    ys = [pos[n][1] for n in ndg.nodes()]
    zs = [pos[n][2] for n in ndg.nodes()]

    ax.scatter(xs, ys, zs, s=80, color="lightgreen")

    for src, dst in ndg.edges():
        x = [pos[src][0], pos[dst][0]]
        y = [pos[src][1], pos[dst][1]]
        z = [pos[src][2], pos[dst][2]]
        ax.plot(x, y, z, color="gray")

    ax.set_title("Réseau tétracordique (3D)")
    return fig


def get_visualisation_list():
    return list(VISUALISATIONS.keys())


# ---------------------------------------------------------
# 4) REGISTRE DES VISUALISATIONS (évolutif)
# ---------------------------------------------------------
VISUALISATIONS = {
    "Hiérarchie verticale": plot_vertical,
    "Constellation circulaire": plot_constellation,
    "Réseau 3D": plot_network_3d,  # sera implémenté plus tard
}
