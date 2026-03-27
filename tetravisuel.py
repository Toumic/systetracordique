# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module tetravisuel : assemble et exporte un JSON complet du système tétracordique

import json


def build_tetra_json(
        gammes,
        tetrachords,
        t_global,
        t_ordre,
        relations,
        t_inf,
        t_sup
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
        "relations": relations  # miror, clone, juxta, symet, diato
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
        t_sup
    )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Fichier JSON exporté : {filename}")
