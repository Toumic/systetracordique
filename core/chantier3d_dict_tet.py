# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module chantier : lance la construction 3d de dict_tet

import matplotlib.pyplot as plt
from typing import Any
import inspect


def debug_line():
    frame = inspect.currentframe()
    # noinspection PyUnresolvedReferences
    return frame.f_back.f_lineno if frame and frame.f_back else -1


# Déclaration du dictionnaire à distribuer
dict_tet = {
    '1234': [('1234', '1234000005678', '1234'), ('1234', '1234000560078', '120034'),
             ('1234', '1234000506078', '102034'), ('1234', '1234000500678', '100234'),
             ('1234', '1234005006078', '1002034'), ('1234', '1234050006078', '10002034'),
             ('1234', '1234500006078', '100002034'), ('123004', '1230040005678', '1234'),
             ('10234', '1023400005678', '1234'), ('102034', '1020340005678', '1234'),
             ('1020304', '1020304005678', '1234'), ('10203004', '1020300405678', '1234'),
             ('102030004', '1020300045678', '1234'), ('1020034', '1020034005678', '1234'),
             ('102003004', '1020030045678', '1234'), ('102000034', '1020000345678', '1234'),
             ('100234', '1002340005678', '1234')],
    '120034': [('120034', '1200340560078', '120034'), ('1234', '1234000560078', '120034'),
               ('120034', '1200340056078', '12034'), ('120034', '1200345600078', '1200034'),
               ('120034', '1200340506078', '102034'), ('120034', '1200340500678', '100234'),
               ('120034', '1200345006078', '1002034'), ('102304', '1023040560078', '120034'),
               ('102034', '1020340560078', '120034'), ('100234', '1002340560078', '120034'),
               ('1000234', '1000234560078', '120034')],
    '102034': [('102034', '1020340506078', '102034'), ('1234', '1234000506078', '102034'),
               ('12304', '1230400506078', '102034'), ('123004', '1230040506078', '102034'),
               ('12034', '1203400506078', '102034'), ('120304', '1203040506078', '102034'),
               ('120034', '1200340506078', '102034'), ('10234', '1023400506078', '102034'),
               ('102304', '1023040506078', '102034'), ('102034', '1020340005678', '1234'),
               ('102034', '1020340560078', '120034'), ('102034', '1020345600078', '1200034'),
               ('102034', '1020340050678', '10234'), ('102034', '1020345060078', '1020034'),
               ('102034', '1020340500678', '100234'), ('102034', '1020345006078', '1002034'),
               ('102034', '1020345000678', '1000234'), ('100234', '1002340506078', '102034')],
    '100234': [('100234', '1002340500678', '100234'), ('1234', '1234000500678', '100234'),
               ('123004', '1230040500678', '100234'), ('120034', '1200340500678', '100234'),
               ('10234', '1023400500678', '100234'), ('102304', '1023040500678', '100234'),
               ('102034', '1020340500678', '100234'), ('100234', '1002340005678', '1234'),
               ('100234', '1002340560078', '120034'), ('100234', '1002340506078', '102034'),
               ('100234', '1002345006078', '1002034')],
    '1002034': [('1234', '1234005006078', '1002034'), ('123004', '1230045006078', '1002034'),
                ('120034', '1200345006078', '1002034'), ('10234', '1023405006078', '1002034'),
                ('102304', '1023045006078', '1002034'), ('102034', '1020345006078', '1002034'),
                ('100234', '1002345006078', '1002034')],
    '10002034': [('1234', '1234050006078', '10002034'), ('12304', '1230450006078', '10002034'),
                 ('12034', '1203450006078', '10002034'), ('10234', '1023450006078', '10002034')],
    '100002034': [('1234', '1234500006078', '100002034')],
    '12304': [('12304', '1230400506078', '102034'), ('12304', '1230450006078', '10002034')],
    '123004': [('123004', '1230040005678', '1234'), ('123004', '1230040056078', '12034'),
               ('123004', '1230040506078', '102034'), ('123004', '1230040500678', '100234'),
               ('123004', '1230045006078', '1002034')],
    '12034': [('123004', '1230040056078', '12034'), ('12300004', '1230000456078', '12034'),
              ('12034', '1203400506078', '102034'), ('12034', '1203450006078', '10002034'),
              ('120034', '1200340056078', '12034'), ('10234', '1023400056078', '12034'),
              ('102304', '1023040056078', '12034'), ('10230004', '1023000456078', '12034'),
              ('10200304', '1020030456078', '12034'), ('10200034', '1020003456078', '12034'),
              ('10020034', '1002003456078', '12034'), ('10000234', '1000023456078', '12034')],
    '12300004': [('12300004', '1230000456078', '12034')], '120304': [('120304', '1203040506078', '102034')],
    '1200034': [('120034', '1200345600078', '1200034'), ('10234', '1023405600078', '1200034'),
                ('102034', '1020345600078', '1200034')],
    '10234': [('10234', '1023400005678', '1234'), ('10234', '1023400056078', '12034'),
              ('10234', '1023405600078', '1200034'), ('10234', '1023456000078', '12000034'),
              ('10234', '1023400506078', '102034'), ('10234', '1023450600078', '10200034'),
              ('10234', '1023400500678', '100234'), ('10234', '1023405006078', '1002034'),
              ('10234', '1023450006078', '10002034'), ('102034', '1020340050678', '10234'),
              ('10203004', '1020300450678', '10234'), ('10200034', '1020003450678', '10234')],
    '12000034': [('10234', '1023456000078', '12000034')],
    '10200034': [('10234', '1023450600078', '10200034'), ('10200034', '1020003456078', '12034'),
                 ('10200034', '1020003450678', '10234')],
    '102304': [('102304', '1023040056078', '12034'), ('102304', '1023040560078', '120034'),
               ('102304', '1023040506078', '102034'), ('102304', '1023040500678', '100234'),
               ('102304', '1023045006078', '1002034')], '10230004': [('10230004', '1023000456078', '12034')],
    '1020034': [('102034', '1020345060078', '1020034'), ('1020034', '1020034005678', '1234')],
    '1000234': [('102034', '1020345000678', '1000234'), ('1000234', '1000234560078', '120034')],
    '1020304': [('1020304', '1020304005678', '1234')],
    '10203004': [('10203004', '1020300405678', '1234'), ('10203004', '1020300450678', '10234')],
    '102030004': [('102030004', '1020300045678', '1234')], '10200304': [('10200304', '1020030456078', '12034')],
    '102003004': [('102003004', '1020030045678', '1234')],
    '102000034': [('102000034', '1020000345678', '1234')], '10020034': [('10020034', '1002003456078', '12034')],
    '10000234': [('10000234', '1000023456078', '12034')]
}


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
joy_registry = []  # ancien j_traces


def apply_9_mask(scale, mask_chars):
    out = ""
    for ch in scale:
        out += "9" if ch in mask_chars else ch
    return out


def find_rich_relation(scale):
    """Cherche une relation riche dans scale_registry."""
    if scale not in scale_registry:
        return None

    y0, z_pair = scale_registry[scale][2]
    z_low, z_high = z_pair
    _ = z_low, z_high  # utilisé implicitement dans le registre
    low_idx = scale_registry[scale][0][1]
    high_idx = scale_registry[scale][1][1]

    for key, val in scale_registry.items():
        if key == scale:
            continue

        if val[0][1] == low_idx:
            return apply_9_mask(scale, "1234"), key

        if val[1][1] == high_idx:
            return apply_9_mask(scale, "5678"), key

    return None


def draw_scale(scale, y, z, ax):
    count_9, tab_9 = 0, []
    for x, ch in enumerate(scale):
        ch0 = ch

        # Pour que le tétracorde comprenant les neuf ait ses intervalles invisibles.
        if ch == "9" and count_9 < 4 and x not in tab_9:
            count_9 += 1  # Compte le nombre de neuf
            tab_9.append(x)
        if tab_9 and x <= max(tab_9):
            ch0 = "9"

        col = degree_color(ch0)
        (debug_line(), "scatter:", (x, y, z), "col:", ch, col, "tab_9", tab_9, ch0)
        ax.scatter(x, y, z, color=col, alpha=1 if col != "white" else 0)


def draw_link(ax, x1, x2, y1, y2, z1, z2):
    (debug_line(), "link:", (x1, y1, z1), "→", (x2, y2, z2))
    # Liaison SYM → JOY INF
    ax.plot([x1, x2], [y1, y2], [z1, z2], color="green")


def build_tetra_scene(tetra_groups, key, ax):
    global scale_registry, joy_registry

    sym_scales, joy_pairs, low_scales, high_scales = tetra_groups[key]

    # --- SYM (gamme de référence)
    if not scale_registry:
        ref = sym_scales[0]
        ref_scale = extract_scale(ref)

        x_sym, y_sym, z_sym = 0, 0, 0

        draw_scale(ref_scale, y_sym, z_sym, ax)

        x_low_sym: int | None = find_index(ref_scale, "4")
        x_high_sym: int | None = find_index(ref_scale, "5")

        trans = normalize_5678(ref_scale[x_high_sym:])

        # SYM enregistré avec Z=0 pour JOY
        # noinspection PyUnresolvedReferences
        scale_registry[ref_scale] = (
            (ref_scale[:x_low_sym + 1], x_low_sym),
            (trans, x_high_sym),
            (y_sym, (0, 0))
        )

    # --- JOY
    z_joy = - 1
    for idx, (low_t, high_t) in enumerate(joy_pairs, start=1):

        # JOY autour du SYM via Y uniquement
        y_low = idx * 1
        y_high = -idx * 1

        z_low, z_high = z_joy, z_joy

        low_scale = extract_scale(low_t)
        high_scale = extract_scale(high_t)
        (debug_line(), "JOY idx:", idx, "low:", low_scale, "high:", high_scale)

        # --- INF
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
                (y_low, (z_low, z_high))
            )

            rel = find_rich_relation(low_scale)  # rel: ('9999000506078', '1234000005678')
            if rel:
                target_z = 0  # z_low
                vrai = [n for n in rel if "9" in n][0]

                (debug_line(), "JOY-INF low_scale:", low_scale, "rel:", rel)
                draw_scale(vrai, y_low, z_low, ax)

                print(debug_line(), "JOY-INF:", f_low, f_low, y_low, y_low, z_low, target_z)
                draw_link(ax, f_low, f_low, y_low, y_low, z_low, target_z)

        # --- SUP
        x_high: int | None = find_index(high_scale, "5")
        f_high: int | None = find_index(high_scale, "4")
        if x_high is None or f_high is None:
            continue

        if high_scale not in scale_registry:
            trans = normalize_5678(high_scale[x_high:])
            scale_registry[high_scale] = (
                (high_scale[:f_high + 1], f_high),
                (trans, x_high),
                (y_high, (z_low, z_high))
            )

            rel = find_rich_relation(high_scale)  # rel: ('9999000506078', '1234000005678')
            if rel:
                target_z = 0  # z_high
                vrai = [n for n in rel if "9" in n][0]

                (debug_line(), "JOY-SUP high_scale:", high_scale, "rel:", rel, vrai)
                draw_scale(vrai, y_high, z_high, ax)

                print(debug_line(), "JOY-SUP:", f_low, f_high, y_low, y_high, z_low, target_z)
                draw_link(ax, f_low, f_high, y_low, y_high, z_low, target_z)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.view_init(elev=20, azim=-60)

    ax.set_yticks([0])
    ax.set_yticklabels(["axe k"])
    ax.set_title(f"Structure tétracordique autour de {key}")


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



def run_scene():
    fig = plt.figure(figsize=(10, 6))
    ax: Any = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-0.05, 0.02)

    tetra_groups = {}

    for k in dict_tet.keys():
        sym_scales = []
        low_scales = []
        high_scales = []
        joy_pairs = []

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

        build_tetra_scene(tetra_groups, k, ax)
        break

    set_equal_aspect_3d(ax)

    plt.show()


if __name__ == "__main__":
    run_scene()
