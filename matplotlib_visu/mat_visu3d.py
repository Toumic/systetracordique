# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module mat_visu3D :
"""
Description :
    Exemple pédagogique montrant comment :
    - créer une figure Matplotlib en 3D
    - placer des notes (points) dans l'espace
    - afficher des labels
    - tracer des liaisons entre notes
    Ce fichier sert de base pour comprendre comment construire
    des visualisations musicales en 3D.
"""

import json
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import inspect
from typing import Callable

# lino() : suivi des étapes internes (trace légère, non intrusive)
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


def exemple_notes_3d(distri, orgo, ordo):
    """
    Exemple simple :
    - une gamme principale (notes verticales)
    - une gamme liée placée à droite
    - des liaisons entre notes identiques

    Cet exemple n'utilise aucune donnée JSON.
    Il sert uniquement à comprendre la mécanique en 3D.
    """

    # ---------------------------------------------------------
    # 1) Création de la figure 3D
    # ---------------------------------------------------------
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # ---------------------------------------------------------
    # Création de la série des tétracordes selon une ordonnance
    # et un rassemblement général donné.
    # ---------------------------------------------------------

    # --- État partagé entre les callbacks et la boucle ---
    etat = {"mode": "original"}  # valeur par défaut

    # --- Bouton ORIGINAL ---
    ax_button_org = plt.axes((0.1, 0.90, 0.1, 0.05))
    btn_org = Button(ax_button_org, "Original")

    # --- Bouton ORDINAL ---
    ax_button_ord = plt.axes((0.2, 0.90, 0.1, 0.05))
    btn_ord = Button(ax_button_ord, "Ordinal")

    # --- Callback : clic sur ORIGINAL ---
    def on_original(_):
        etat["mode"] = "original"
        print("Mode =", etat["mode"])
        rafraichir()

    # --- Callback : clic sur ORDINAL ---
    def on_ordinal(_):
        etat["mode"] = "ordinal"
        print("Mode =", etat["mode"])
        rafraichir()

    btn_org.on_clicked(on_original)
    btn_ord.on_clicked(on_ordinal)

    # --- Fonction qui redessine selon le mode ---
    def rafraichir():
        ax.clear()

        if etat["mode"] == "original":
            ooo = orgo
        else:
            ooo = ordo

        # Construction de la table de lecture.

        for oo in ooo:
            for odo in distri[oo]:
                print(lineno(), "oo", oo, "odo", odo)
                break

        print(lineno(), "orgo", orgo, "\ndistri", distri[orgo[0]])

    # ---------------------------------------------------------
    # 2) Définition des notes (hauteurs arbitraires)
    #    Dans ton vrai projet, ces valeurs viendront du JSON.
    # ---------------------------------------------------------
    notes_principale = [0, 2, 4, 5, 7, 9, 11]      # gamme principale
    notes_liee = [5, 7, 9, 11, 12, 14, 16]         # gamme liée

    # Position horizontale (axe X)
    x_main = 0
    x_liee = 1.5

    # Position en profondeur (axe Z)
    # Ici, on reste sur une seule strate (z = 0)
    z_main = 0
    z_liee = 0

    # ---------------------------------------------------------
    # 3) Affichage de la gamme principale
    # ---------------------------------------------------------
    for h in notes_principale:
        # Point représentant la note
        ax.scatter(x_main, h, z_main, s=200, color="orange")

        # Label de la note
        ax.text(x_main, h, z_main, str(h),
                ha="center", va="center", fontsize=10)

    # ---------------------------------------------------------
    # 4) Affichage de la gamme liée
    # ---------------------------------------------------------
    for h in notes_liee:
        ax.scatter(x_liee, h, z_liee, s=200, color="lightgray")
        ax.text(x_liee, h, z_liee, str(h),
                ha="center", va="center", fontsize=10)

    # ---------------------------------------------------------
    # 5) Tracer des liaisons entre notes identiques
    #    Ici : 5, 7, 9, 11 sont communes aux deux gammes.
    # ---------------------------------------------------------
    notes_communes = [5, 7, 9, 11]

    for h in notes_communes:
        ax.plot(
            [x_main, x_liee],   # X : de la gamme principale à la gamme liée
            [h, h],             # Y : même hauteur
            [z_main, z_liee],   # Z : même strate
            color="black",
            linewidth=2
        )

    # ---------------------------------------------------------
    # 6) Réglages visuels
    # ---------------------------------------------------------
    ax.set_xlabel("Position X")
    ax.set_ylabel("Hauteur (valeurs JSON)")
    ax.set_zlabel("Strate (Z)")

    # Optionnel : meilleure lisibilité
    ax.view_init(elev=20, azim=30)

    plt.title("Exemple pédagogique : placement de notes et liaisons en 3D")
    plt.show()


def charger_json(nom_fichier):
    """
    Charge un fichier JSON situé dans le dossier data.
    Retourne un dictionnaire Python.
    """

    # Dossier où se trouve ce fichier (matplotlib_visu)
    dossier_courant = os.path.dirname(__file__)

    # Racine du projet (un niveau au-dessus)
    racine = os.path.abspath(os.path.join(dossier_courant, ".."))

    # Chemin complet vers json_data/nom_fichier
    chemin_json = os.path.join(racine, "data", nom_fichier)

    with open(chemin_json, "r", encoding="utf-8") as f:
        return json.load(f)


def exemple_chargement():
    """
    Exemple simple montrant comment charger un fichier JSON
    et afficher son contenu.
    """

    gamme = charger_json("tetracorde.json")

    # Organiser un dictionnaire utilitaire.
    ("#'gammes' = gamme {'o45x': '123400000567', 'o46-': '123400056007', 'o4': '123400050607'...],"
     "'tetrachords' = voir définition : systetra.py lignes (15, 16, 17, 18),"
     "'positions' = détails des position inf/sup, par tétra-clé et valeurs nom-gamme et gamme et position,"
     "'relations' = voir définition : globaliste.py lignes (12, 13, 14, 15),"
     "'diatonies' = 'o45x': {['C', '-D', 'oE', 'oF', 'xG', '+A', 'B']...}. Nom-clé, valeur gamme en lettres signées,"
     "'distribution' = partie intégrale des clés-tétras, aux valeurs inf/gamme/sup,"
     "'original' = ordre original des apparitions tétracordiques,"
     "'ordinal' = tri décroissant de l'ordre original")

    # Liste des clés tétras originales
    k_org = [k for k in gamme['original'].keys()]  # Ordre naturel de la séquence des clés tétras.
    k_ord = [k for k in gamme['ordinal'].keys()]  # Ordre décroissant de la séquence des clés tétras.

    (lineno(), "original", gamme['original'])
    exemple_notes_3d(gamme['distribution'], k_org, k_ord)

    # dict_keys(['gammes', 'tetrachords', 'positions', 'relations', 'diatonies', 'distribution', 'original', 'ordinal'])
    (lineno(), "Notes :", gamme['original'])


if __name__ == "__main__":
    exemple_chargement()
