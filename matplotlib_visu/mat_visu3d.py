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
from pathlib import Path
import matplotlib.pyplot as plt
from typing import Any
import inspect


def debug_line():
    frame = inspect.currentframe()
    # noinspection PyUnresolvedReferences
    return frame.f_back.f_lineno if frame and frame.f_back else -1



def find_index(scale, target):
    try:
        return scale.index(target)
    except ValueError:
        return None


def normalize_5678(segment):
    out = ""
    n = 1
    for ch in segment:
        if ch == "0":
            out += "0"
        else:
            out += str(n)
            n += 1
    return out


def degree_color(ch):
    if ch in "1234":
        return "red"
    if ch == "0":
        return "orange"
    if ch in "5678":
        return "blue"
    if ch == "9":
        return "white"  # invisible
    return "black"


def extract_scale(tetra):
    for item in tetra:
        if isinstance(item, str) and len(item) == 13:
            return item
    raise ValueError("Aucun degré complet trouvé")


scale_registry = {}  # ancien t_traces
ancien_tetra = ""  # Hiérarchie antérieure


def apply_9_mask(scale, mask_chars):
    # Normalisation : scale peut être un string, un tuple de 1, ou un tuple de 2.
    if isinstance(scale, str):
        originals = (scale,)
    else:
        originals = tuple(scale)

    # Fonction interne de masquage
    def mask_string(s):
        return "".join("9" if c in mask_chars else c for c in s)

    # Masquage de tous les originaux
    masked = tuple(mask_string(s) for s in originals)

    # --- Décision finale ---
    if len(masked) == 1:
        # Cas simple : un seul tétra → tuple plat
        return masked[0], originals[0]

    # Cas multiple : deux tétras → tuple de tuples
    return masked, originals


def find_rich_relation(scale):
    """Cherche une relation riche dans scale_registry."""
    global ancien_tetra

    if scale not in scale_registry.keys():
        return None

    low_idx = scale_registry[scale][0][0]
    high_idx = scale_registry[scale][1][0]
    ancien_tetra = ""

    # Déclaration des utilités puisque les deux tétras peuvent déjà être référencés
    scale1234, s1234, key1 = "", True, ""  # Tétra inférieur
    scale5678, s5678, key5 = "", True, ""  # Tétra supérieur

    for key, val in scale_registry.items():
        if key == scale:
            continue

        if val[0][0] == low_idx and s1234:
            scale1234, s1234, key1 = scale, False, key

        if val[1][0] == high_idx and s5678:
            scale5678, s5678, key5 = scale, False, key

        if key1 and key5:
            break

    if key1 and key5:
        ancien_tetra = key1, key5
        return apply_9_mask(ancien_tetra, "12345678")
    elif key1:
        ancien_tetra = key1
        return apply_9_mask(ancien_tetra, "1234")
    elif key5:
        ancien_tetra = key5
        return apply_9_mask(ancien_tetra, "5678")

    return None


def draw_scale(scale, y, z, ax):
    for x, ch in enumerate(scale):
        col = degree_color(ch)
        (debug_line(), "scatter:", scale, (x, y, z), "col:", ch, col)
        ax.scatter(x, y, z, color=col, alpha=1, s=5 if col != "white" else 0)


def draw_link(ax, x1, x2, y1, y2, z1, z2, tip):
    (debug_line(), "link:", (x1, y1, z1), "→", (x2, y2, z2))
    # Coloration des liaisons
    if tip == "1":
        couleur = "green"
    else:
        couleur = "black"
    ax.plot([x1, x2], [y1, y2], [z1, z2], color=couleur, linewidth=0.5)


def build_tetra_scene(tetra_groups, key, ax, current_depth):
    global scale_registry

    sym_scales, joy_pairs, low_scales, high_scales = tetra_groups[key]

    # --- SYM (gamme de référence)
    if sym_scales:  # not scale_registry
        ref = sym_scales[0]
        ref_scale = extract_scale(ref)

        x_sym, y_sym, z_sym = 0, 0, current_depth

        x_low_sym: int | None = find_index(ref_scale, "4")
        x_high_sym: int | None = find_index(ref_scale, "5")

        trans = normalize_5678(ref_scale[x_high_sym:])

        # SYM enregistré avec Z=0 pour JOY
        # noinspection PyUnresolvedReferences
        scale_registry[ref_scale] = (
            (ref_scale[:x_low_sym + 1], x_low_sym),
            (trans, x_high_sym),
            (y_sym, (z_sym, z_sym))
        )

        if len(scale_registry) > 1:

            rel = find_rich_relation(ref_scale)  # rel: ('9999000506078', '1234000005678')
            if rel and isinstance(rel[0], tuple):
                # Section 1
                i_xyz1 = scale_registry[rel[1][0]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[ref_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][0], y_sym, z_sym, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")

                # Section 2
                i_xyz1 = scale_registry[rel[1][1]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[ref_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][1], y_sym, z_sym, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")
            else:
                if rel:
                    i_xyz1 = scale_registry[rel[1]]
                    i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                    i_xyz2 = scale_registry[ref_scale]
                    i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                    draw_scale(rel[0], y_sym, z_sym, ax)
                    draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "1")
        else:
            draw_scale(ref_scale, y_sym, z_sym, ax)

    # --- JOY
    z_joy = current_depth - 1
    for idx, (low_t, high_t) in enumerate(joy_pairs, start=1):

        # JOY autour du SYM via Y uniquement
        y_low = idx * 1
        y_high = -idx * 1

        z_low, z_high = z_joy, z_joy

        low_scale = extract_scale(low_t)
        high_scale = extract_scale(high_t)
        (debug_line(), "JOY idx:", idx, "low:", low_scale, "high:", high_scale)

        # --- JOY-INF
        x_low: int | None = find_index(low_scale, "4")
        f_low: int | None = find_index(low_scale, "5")
        if x_low is None or f_low is None:
            continue

        (debug_line(), "JOY scale_registry:", scale_registry)
        if low_scale not in scale_registry:
            trans = normalize_5678(low_scale[f_low:])
            scale_registry[low_scale] = (
                (low_scale[:x_low + 1], x_low),
                (trans, f_low),
                (y_low, (z_low, z_low))
            )

            rel = find_rich_relation(low_scale)  # rel: ('9999000506078', '1234000005678')
            if rel and isinstance(rel[0], tuple):
                (debug_line(), "REL multiple:", rel)
                # Section 1
                i_xyz1 = scale_registry[rel[1][0]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[low_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][0], y_low, z_low, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")

                # Section 2
                i_xyz1 = scale_registry[rel[1][1]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[low_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][1], y_low, z_low, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")
            else:
                (debug_line(), "REL simple:", rel)
                if rel:
                    i_xyz1 = scale_registry[rel[1]]
                    i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                    i_xyz2 = scale_registry[low_scale]
                    i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                    draw_scale(rel[0], y_low, z_low, ax)
                    draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "1")

        # --- JOY-SUP
        x_high: int | None = find_index(high_scale, "5")
        f_high: int | None = find_index(high_scale, "4")
        if x_high is None or f_high is None:
            continue

        if high_scale not in scale_registry:
            trans = normalize_5678(high_scale[x_high:])
            scale_registry[high_scale] = (
                (high_scale[:f_high + 1], f_high),
                (trans, x_high),
                (y_high, (z_low, z_low))
            )

            rel = find_rich_relation(high_scale)  # rel: ('9999000506078', '1234000005678')
            if rel and isinstance(rel[0], tuple):
                (debug_line(), "REL multiple:", rel)
                # Section 1
                i_xyz1 = scale_registry[rel[1][0]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[high_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][0], y_high, z_high, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")

                # Section 2
                i_xyz1 = scale_registry[rel[1][1]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[high_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][1], y_high, z_high, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")
            else:
                (debug_line(), "REL simple:", rel)
                if rel:
                    s_xyz1 = scale_registry[rel[1]]
                    s_x1, s_y1, s_z1 = s_xyz1[0][1], s_xyz1[2][0], s_xyz1[2][1][0]
                    s_xyz2 = scale_registry[high_scale]
                    s_x2, s_y2, s_z2 = s_xyz2[0][1] + 1, s_xyz2[2][0], s_xyz2[2][1][0]

                    draw_scale(rel[0], y_high, z_high, ax)
                    draw_link(ax, s_x1, s_x2, s_y1, s_y2, s_z1, s_z2, "1")

    # --- Après la boucle JOY
    n_joy = len(joy_pairs)

    # Dernières positions Y des JOY
    last_joy_low_y = +n_joy
    last_joy_high_y = -n_joy

    # Profondeur progressive
    z_orphan_base = current_depth - 1
    z_orphan_step = - 0.1  # Valeur de l'intervalle Z entre les orphelins

    # --- LOW_SCALES
    for i, lo_t in enumerate(low_scales, start=1):
        low_scale = extract_scale(lo_t)

        # même colonne Y que JOY-INF
        y_low_orphan = last_joy_low_y + i

        # descente progressive en 'Z'
        z_low_orphan = z_orphan_base + i * z_orphan_step

        x_low: int | None = find_index(low_scale, "4")
        f_low: int | None = find_index(low_scale, "5")
        if x_low is None or f_low is None:
            continue

        (debug_line(), "JOY scale_registry:", scale_registry)
        if low_scale not in scale_registry:
            trans = normalize_5678(low_scale[f_low:])
            scale_registry[low_scale] = (
                (low_scale[:x_low + 1], x_low),
                (trans, f_low),
                (y_low_orphan, (z_low_orphan, z_low_orphan))
            )

            rel = find_rich_relation(low_scale)  # rel: ('9999000506078', '1234000005678')
            if rel and isinstance(rel[0], tuple):
                (debug_line(), "REL multiple:", rel)
                # Section 1
                i_xyz1 = scale_registry[rel[1][0]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[low_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][0], y_low_orphan, z_low_orphan, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")

                # Section 2
                i_xyz1 = scale_registry[rel[1][1]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[low_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][1], y_low_orphan, z_low_orphan, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")
            else:
                (debug_line(), "REL simple:", rel)
                if rel:
                    i_xyz1 = scale_registry[rel[1]]
                    i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                    i_xyz2 = scale_registry[low_scale]
                    i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                    draw_scale(rel[0], y_low_orphan, z_low_orphan, ax)
                    draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "1")

    # --- HIGH_SCALES
    for j, hi_t in enumerate(high_scales, start=1):
        high_scale = extract_scale(hi_t)

        # même colonne Y que JOY-SUP
        y_high_orphan = last_joy_high_y - j

        # descente progressive en 'Z'
        z_high_orphan = z_orphan_base + j * z_orphan_step

        x_high: int | None = find_index(high_scale, "5")
        f_high: int | None = find_index(high_scale, "4")
        if x_high is None or f_high is None:
            continue

        if high_scale not in scale_registry:
            trans = normalize_5678(high_scale[x_high:])
            scale_registry[high_scale] = (
                (high_scale[:f_high + 1], f_high),
                (trans, x_high),
                (y_high_orphan, (z_high_orphan, z_high_orphan))
            )

            rel = find_rich_relation(high_scale)  # rel: ('9999000506078', '1234000005678')
            if rel and isinstance(rel[0], tuple):
                (debug_line(), "REL multiple:", rel)
                # Section 1
                i_xyz1 = scale_registry[rel[1][0]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[high_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][0], y_high_orphan, z_high_orphan, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")

                # Section 2
                i_xyz1 = scale_registry[rel[1][1]]
                i_x1, i_y1, i_z1 = i_xyz1[1][1], i_xyz1[2][0], i_xyz1[2][1][0]
                i_xyz2 = scale_registry[high_scale]
                i_x2, i_y2, i_z2 = i_xyz2[1][1] - 1, i_xyz2[2][0], i_xyz2[2][1][0]

                draw_scale(rel[0][1], y_high_orphan, z_high_orphan, ax)
                draw_link(ax, i_x1, i_x2, i_y1, i_y2, i_z1, i_z2, "2")
            else:
                (debug_line(), "REL simple:", rel)
                if rel:
                    s_xyz1 = scale_registry[rel[1]]
                    s_x1, s_y1, s_z1 = s_xyz1[0][1], s_xyz1[2][0], s_xyz1[2][1][0]
                    s_xyz2 = scale_registry[high_scale]
                    s_x2, s_y2, s_z2 = s_xyz2[0][1] + 1, s_xyz2[2][0], s_xyz2[2][1][0]

                    draw_scale(rel[0], y_high_orphan, z_high_orphan, ax)
                    draw_link(ax, s_x1, s_x2, s_y1, s_y2, s_z1, s_z2, "1")

    # --- FIN de build_tetra_scene
    depth_used = -(6 + max(len(low_scales), len(high_scales)) * abs(z_orphan_step))

    return current_depth + depth_used


def set_equal_aspect_3d(ax):
    x = ax.get_xlim3d()
    y = ax.get_ylim3d()
    z = ax.get_zlim3d()

    dx = float(abs(x[1] - x[0]))
    dy = float(abs(y[1] - y[0]))
    dz = float(abs(z[1] - z[0]))

    max_range = max(dx, dy, dz) / 2.0

    mid_x = (x[0] + x[1]) / 2
    mid_y = (y[0] + y[1]) / 2
    mid_z = (z[0] + z[1]) / 2

    ax.set_xlim3d(mid_x - max_range, mid_x + max_range)
    ax.set_ylim3d(mid_y - max_range, mid_y + max_range)
    ax.set_zlim3d(mid_z - max_range, mid_z + max_range)


def run_scene(dict_tet, et1, et2):
    fig = plt.figure(figsize=(7, 5))
    plt.tight_layout()
    ax: Any = fig.add_subplot(111, projection='3d')
    (et1, et2)

    # Profondeur de base
    current_depth = 0

    tetra_groups = {}

    clef, cc = [], 0

    for k in dict_tet.keys():
        sym_scales = []
        low_scales = []
        high_scales = []
        joy_pairs = []
        clef.append(k)
        cc += 1

        for entry in dict_tet[k]:
            if entry[0] == entry[-1] == k:
                sym_scales.append(entry)
            elif entry[0] == k:
                high_scales.append(entry[1:])
            else:
                low_scales.append(entry[:2])

        for low in low_scales:
            for high in high_scales:
                if low[0] in high:
                    joy_pairs.append((low, high))
                    low_scales.remove(low)
                    high_scales.remove(high)

        tetra_groups[k] = [sym_scales, joy_pairs, low_scales, high_scales]

        current_depth = build_tetra_scene(tetra_groups, k, ax, current_depth)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    # 'elev' = hauteur caméra, 'azim' rotation horizontale
    ax.view_init(elev=10, azim=-15)

    ax.set_yticks([0])
    ax.set_yticklabels(["axe k"])
    ax.set_title(f"Structure tétracordique autour de {clef[0]}")

    set_equal_aspect_3d(ax)

    plt.show()


def charger_json(nom_fichier):
    """
    Charge un fichier JSON situé dans le dossier data.
    Retourne un dictionnaire Python.
    """

    # Dossier où se trouve ce fichier (matplotlib_visu)
    dossier_courant = Path(__file__).parent

    # Racine du projet (un niveau au-dessus)
    racine = dossier_courant.parent

    # Chemin complet vers data/nom_fichier
    chemin_json = racine / "data" / nom_fichier

    with chemin_json.open("r", encoding="utf-8") as f:
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

    (debug_line(), "original", gamme['original'])
    run_scene(gamme['distribution'], k_org, k_ord)

    # dict_keys(['gammes', 'tetrachords', 'positions', 'relations', 'diatonies', 'distribution', 'original', 'ordinal'])
    (debug_line(), "Notes :", gamme['original'])


if __name__ == "__main__":
    exemple_chargement()
