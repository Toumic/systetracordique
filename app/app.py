# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module app

import gradio as gr
from visual.visualisation import VISUALISATIONS
# from visual.visualisation import plot_vertical, plot_constellation, plot_network_3d

# Tu chargeras tes données ici :
from data import tetracorde   # Exemple


def run_visualisation(selected):
    func = VISUALISATIONS[selected]
    fig = func(t_ordre) if selected != "Réseau 3D" else func(t_ordre, relations)
    return fig


with gr.Blocks() as demo:
    gr.Markdown("# Visualisation tétracordique")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Choix de la visual")
            choice = gr.Radio(
                list(VISUALISATIONS.keys()),
                label="Visualisations disponibles"
            )
        with gr.Column(scale=4):
            output = gr.Plot()

    choice.change(run_visualisation, inputs=choice, outputs=output)

demo.launch()
