# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module main : lance la chaîne complète
# systetra → globaliste → tetravisuel

import systetra
import globaliste
import tetravisuel


def main():
    print("→ Calcul des tétracordes…")
    systetra.print_hi()

    # 1. Gammes (noms + énumérations)
    gammes = dict(zip(systetra.n_gam, systetra.e_gam))

    # 2. Tétras
    tetrachords = {
        "union": list(systetra.union_t.keys()),
        "ponton": list(systetra.ponton_t.keys()),
        "super": list(systetra.super_t.keys()),
        "infer": list(systetra.infer_t.keys())
    }

    # 3. Positions inf/sup dans les gammes
    t_global = systetra.t_global

    # 4. Ordre croissant des tétras
    t_ordre = systetra.t_ordre

    # 5. Relations miroir/clone/juxta/symet/diato
    relations = globaliste.dict_miroir_org

    # 6. Tétras inf/sup bruts
    t_inf = systetra.t_inf
    t_sup = systetra.t_sup

    print("→ Export du fichier JSON enrichi…")
    tetravisuel.export_json(
        gammes,
        tetrachords,
        t_global,
        t_ordre,
        relations,
        t_inf,
        t_sup
    )

    print("✓ Processus terminé.")


if __name__ == "__main__":
    main()
