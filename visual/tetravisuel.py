# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module tetravisuel : assemble et exporte un JSON complet du système tétracordique

import json
import os


def build_tetra_json(
        gammes,
        tetrachords,
        t_global,
        t_ordre,
        relations,
        t_inf,
        t_sup,
        diatonies=None,
        distribution=None,
        original=None,
        ordinal=None
):
    """
    Construit la structure JSON complète du système tétracordique.
    Toutes les données sont passées en argument pour éviter les imports circulaires.
    """

    data = {
        "gammes": gammes,  # 66 gammes : nom → énumération
        "tetrachords": {
            "union": tetrachords["union"],
            "ponton": tetrachords["ponton"],
            "super": tetrachords["super"],
            "infer": tetrachords["infer"],
            "ordre": t_ordre,  # ordre croissant des tétras
            "t_inf": t_inf,  # tétras inférieurs bruts
            "t_sup": t_sup  # tétras supérieurs bruts
        },
        "positions": t_global,  # t_global : tétra → positions inf/sup dans les gammes
        "relations": relations,  # clone, juxta, symet, diato
        "diatonies": diatonies,
        "distribution": distribution,
        "original": original,
        "ordinal": ordinal
    }

    return data


def export_json(
        gammes,
        tetrachords,
        t_global,
        t_ordre,
        relations,
        t_inf,
        t_sup,
        diatonies=None,
        distribution=None,
        original=None,
        ordinal=None,
        filename="tetracorde.json"
):
    """
    Exporte le JSON complet dans un fichier.
    """

    data = build_tetra_json(
        gammes,
        tetrachords,
        t_global,
        t_ordre,
        relations,
        t_inf,
        t_sup,
        diatonies=diatonies,
        distribution=distribution,
        original=original,
        ordinal=ordinal
    )

    # Dossier où se trouve tetravisuel.py
    dossier_courant = os.path.dirname(__file__)

    # Racine du projet
    racine = os.path.abspath(os.path.join(dossier_courant, ".."))

    # Chemin vers data/
    chemin_json = os.path.join(racine, "data", filename)

    with open(chemin_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
