# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module main : lance la chaîne complète
# systetra → globaliste → tetravisuel

from core import systetra, globaliste
from visual import tetravisuel
from matplotlib_visu import mat_visu3d


def main():
    print("→ Calcul des tétracordes…")
    systetra.compute_tetras()

    # 1. Gammes (noms + énumérations)
    gammes = dict(zip(systetra.n_gam, systetra.e_gam))
    diatonies = dict(zip(systetra.n_gam, systetra.g_gam))
    ("\nGammes :", gammes, len(gammes))

    # 2. Tétras
    tetrachords = {
        "union": list(systetra.union_t.keys()),
        "ponton": list(systetra.ponton_t.keys()),
        "super": list(systetra.super_t.keys()),
        "infer": list(systetra.infer_t.keys())
    }
    ("\nTetrachords :", tetrachords)

    # 3. Positions inf/sup dans les gammes
    t_global = systetra.t_global
    ("\nt_global :", t_global, "→", len(t_global), "éléments")

    # 4. Ordre croissant des tétras
    t_ordre = systetra.t_ordre
    ("\nOrdre des tétras :", t_ordre)

    # 5. Reprises du module globaliste.py
    relations = globaliste.dict_miroir_org
    distribution = globaliste.dict_tet  # Déclaration fondamentale des tétracordes.
    original = globaliste.dict_relate_org  # Déclaration de l'organisation originale.
    ordinal = globaliste.dict_relate_ord  # Déclaration de l'organisation ordonnée.
    ("\nRelations :", relations)

    # 6. Tétras inf/sup bruts
    t_inf = systetra.t_inf
    t_sup = systetra.t_sup
    ("\nInf :", t_inf, "\tSup :", t_sup)

    # ---------------------------------------------------------
    # EXPORT JSON
    # ---------------------------------------------------------
    print("\n→ Export du fichier JSON enrichi…",)
    tetravisuel.export_json(
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
    print("✓ Export terminé.")

    # ---------------------------------------------------------
    # CHOIX LOCAL / WEB
    # ---------------------------------------------------------
    print("\n=== Système tétracordique : visual ===")
    print("1) Interface locale (Matplotlib)")
    print("2) Interface web (Gradio)")
    choix = input("Votre choix : ")

    if choix == "1":
        mat_visu3d.exemple_chargement()
        '''from visual.visualisation import plot_vertical, plot_network_3d
        fig = plot_network_3d(t_ordre, relations)
        fig.show()

        plot_vertical(t_ordre)'''
        input("Appuyez sur Entrée pour fermer…")

    elif choix == "2":
        import os
        os.system("python app/app.py")

    else:
        print("Choix invalide.")

    # Retour structuré (utile pour tests ou interface)
    return {
        "gammes": gammes,
        "tetrachords": tetrachords,
        "t_global": t_global,
        "t_ordre": t_ordre,
        "relations": relations,
        "t_inf": t_inf,
        "t_sup": t_sup
    }


if __name__ == "__main__":
    main()
