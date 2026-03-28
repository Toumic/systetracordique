# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module globaliste : Ce module traite les clés et les contenus du dictionnaire systetra.t_global

import tetravisuel
import inspect
from typing import Callable

# lino() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

dict_miroir_org = {
    "miror": {},
    "clone": {},
    "juxta": {},
    "symet": {},
    "diato": {}
}

def globe(glob):
    """ Ce module a une fonction chargée de constituer algorithmiquement la topographie des tétracordes.
    Une ancienne version papier existe et sa définition visuelle est sur le site : https://www.cabviva.fr/magtet-1.

    Introduction du dictionnaire t_global.
    Détails des introductions :
        # union {'1234': '1234', '12304': '12304', (dico tous les téras), ...} 28
        # ponton {'1234': '1234', (dico les tétras communs aux inf/sup), ...} 9
        # super {'1002034': '1002034', (dicos seuls les tétras supérieurs), ...} 5
        # infer {'12304': '12304', '123004': '123004', '12300004': '12300004', ...] 14
        # t_global['1234'] | '1234': ['o45x.1234000005678.inf', 'o45x.1234000005678.sup', ...]
            * Le dico t_global indexe à chacune de ses clés, les gammes qui possèdent ces clés."""
    ("\n", lineno(), "glob :", glob.keys(), "\n")
    "#  26 glob : dict_keys(['t_inf', 't_sup', 't_global', 'union_t', 'ponton_t', 'super_t', 'infer_t', 't_ordre'])"

    "# Structurer la lecture de t_global"
    "# Création d'un dictionnaire global interne i_global."
    i_global = {}  # La trilogie du tétracorde = [nom_gamme énumérée_position]
    "# La liste des clés de glob['t_global']."
    k_global = glob['t_global'].keys()
    (lineno(), "k_global", k_global, len(k_global))
    # 34 k_global dict_keys(['1234', '120034', '102034', '100234', '1002034', '10002034', ...] 28
    valeurs, v = {}, 0  # Dictionnaire pour les trois valeurs, compteur tétra utiles.
    t_double = {}  # Dico des tétras en double dans une seule gamme.
    v_noms = {}  # Dico à clefs = tétra et valeurs = noms.
    for k_glob in k_global:
        i_global[k_glob] = glob['t_global'][k_glob]
        (lineno(), "k_glob", k_glob, "i_global", i_global[k_glob], len(i_global[k_glob]))
        # 36 k_glob 1234 i_global ['o45x_1234000005678.inf', 'o45x_1234000005678.sup', 'o46-_1234000560078.inf',
        # 'o4_1234000506078.inf', 'o46+_1234000500678.inf', 'o45-_1234005006078.inf', 'o54-_1234050006078.inf',
        # '*5_1234500006078.inf', 'o35x_1230040005678.sup', '-45x_1023400005678.sup', 'x5_1020340005678.sup',
        # '+45x_1020304005678.sup', 'x45+_1020300405678.sup', '^4_1020300045678.sup', '+35x_1020034005678.sup',
        # '+34x_1020030045678.sup', '^3_1020000345678.sup', '+25x_1002340005678.sup'] 18
        v += 1

        "# Sonder les entrées afin de séparer les noms, les énumérations et les inf/sup"
        # a[:a.index('_')] = '-56', a[a.index('.')+1:] = 'inf', a[a.index('_')+1:a.index('.'):] = '1020345060078'
        valeurs[k_glob], v_noms[k_glob] = [], []
        val1, val2, val3 = '', '', ''
        for a in i_global[k_glob]:
            val1 = a[:a.index('_')]  # Nom de la gamme
            val2 = a[a.index('_') + 1:a.index('.'):]  # Forme énumérée de la gamme
            val3 = a[a.index('.') + 1:]  # Position du tétracorde dans la gamme.
            valeurs[k_glob].append((val1, val2, val3))
            v_noms[k_glob].append(val1)  # Dico, clé = tétra et valeur = nom de la gamme
        (lineno(), v, " * k_glob", k_glob, valeurs[k_glob], "v_noms", v_noms[k_glob])
        # 57 1  * k_glob 1234 [('o45x', '1234000005678', 'inf'), ('o45x', '1234000005678', 'sup'), ...]
        # v_noms ['o45x', 'o45x', 'o46-', 'o4', 'o46+', 'o45-', 'o54-', '*5', 'o35x', '-45x', ...]

        "# Répertorier les gammes ayant deux tétracordes identiques en positions inf/sup."
        for a in v_noms[k_glob]:
            if v_noms[k_glob].count(a) > 1:
                t_double[k_glob] = ""
                if a not in t_double[k_glob]:
                    t_double[k_glob] = a
            (lineno(), "Doublons de a", a, t_double)
            # 68 Doublons de a +26 {'1234': 'o45x', '120034': '-26', '102034': '0', '100234': '+26'}
    (lineno(), " * valeurs", valeurs)  # , valeurs = {..., '10000234': [('^2', '1000023456078', 'inf')]}

    ("# Positionner graphiquement les notes des tétras par rapport au tétra naturellement majeur."
     "Le dico dic_tet_maj, clé = tétra, valeur = signe, position, longueur.")
    tet_maj, cnt_tm = "102034", 0  # Version positions réelles = [1, 3, 5, 6]
    dic_tet_maj = {}  # Dico, clef = tétra, valeur = positionnement élémentaire. ([0, 3, 2, 2], [1, 6, 7, 8], 8)
    for kg in k_global:
        dic_tet_maj[kg] = []
        tet_sig, tet_pos, cnt_pos = [], [], 0
        cnt_tm += 1
        (lineno(), "kg", kg)
        for k in kg:
            cnt_pos += 1
            if k != "0":
                pos_m = tet_maj.index(k)
                pos_k = kg.index(k)
                dif_pos = pos_k - pos_m
                tet_sig.append(dif_pos)
                tet_pos.append(cnt_pos)
                (lineno(), "k", k, "pos", pos_m, pos_k, "dif_pos", dif_pos)
        dic_tet_maj[kg] = tet_sig, tet_pos, len(kg)
        (lineno(), "dic_tet_maj", kg, dic_tet_maj[kg], "\t\tcnt_tm", cnt_tm)
        # 92 dic_tet_maj 10000234 ([0, 3, 2, 2], [1, 6, 7, 8], 8) 		cnt_tm 28


    def go_inf(t_val, t_duo, f_val):
        """Fonction chargée de retrouver les parties inférieures ou supérieures
        de la gamme parmi les valeurs et k_global"""
        fv, f_pos = 0, []  # Compteur fv et enregistreur f_pos
        # k_global = Les clefs tétras utiles.
        # Sorties : tétra_inf, gamme_énumérée, tétra_sup.
        # t_val == "dia" a[1][p:] = '560078', de a = ('o46-', '1234000560078', 'inf'), p = a[1].index("5").
        # t_val == "dia" b[1][:s+1] = '123004', de b = ('o35x', '1230040005678', 'sup'), s = b[1].index("4")."
        # print(lineno(), "DEF go_inf t_val", t_val, "t_duo", t_duo, "f_val", f_val)
        for kg in k_global:  # Lecture des clés tétras.
            for kg2 in valeurs[kg]:
                if f_val in kg2:
                    if "inf" in kg2:
                        fv += 1
                        if t_val == "duo":
                            f_pos.append(kg + "inf")
                            (lineno(), "DUO f_pos", f_pos)
                        elif t_val == "dia" and kg == t_duo:
                            p = kg2[1].index("5")
                            s = kg2[1][p:]
                            z0, z1 = 0, ""
                            for x in s:
                                if x != "0":
                                    z0 += 1
                                    z1 += str(z0)
                                else:
                                    z1 += "0"
                            s = z1
                            f_pos.append(s + "sup")
                            (lineno(), fv, "DIA t_duo", t_duo, "p_s", p, s, "\t kg", kg, "kg2", kg2)
                            # 100 1 DIA t_duo 1234 p_s 7 120034 	 kg 1234 kg2 ('o46-', '1234000560078', 'inf')
                        # print(lineno(), "INF kg", kg, "f_pos", f_pos)
                    elif "sup" in kg2:
                        fv += 1
                        if t_val == "duo":
                            f_pos.append(kg + "sup")
                            (lineno(), "DUO f_pos", f_pos)
                        elif t_val == "dia" and kg == t_duo:
                            p = kg2[1].index("4")
                            s = kg2[1][:p+1]
                            f_pos.append(s + "inf")
                            (lineno(), fv, "DIA t_duo", t_duo, "p_s", p, s, "\t kg", kg, "kg2", kg2)
                            # 110 1 DIA t_duo 1234 p_s 5 123004 	 kg 1234 kg2 ('o35x', '1230040005678', 'sup')
                        # print(lineno(), "SUP kg", kg, "f_pos", f_pos)
                if fv == 2:
                    ("\n", lineno(), "f_val", f_val, "tétras kg kg2", kg, kg2, "f_pos", f_pos)
                    # 113 f_val 1234000560078 tétras kg kg2 120034 ('o46-', '1234000560078', 'sup') f_pos ['120034sup']
                    if t_val == "dia":
                        (lineno(), "inf", kg, t_duo)
                        don_num = f_val  # retour_t[0]
                        it = f_pos[0]  # retour_t[1][0]
                        (lineno(), "it", it, "f_pos", f_pos)
                        if "inf" in it:  # retour_t[1][0]
                            don_inf = it[:len(it) - 3]
                            don_sup = t_duo
                            (lineno(), "inf kg", kg, "don_inf, don_sup", don_inf, don_sup)
                        elif "sup" in it:
                            don_inf = t_duo
                            don_sup = it[:len(it) - 3]
                            (lineno(), "sup kg", kg, "don_inf, don_sup", don_inf, don_sup)
                        (lineno(), "RETURN duo", duo, "don_inf, don_num, don_sup", don_inf, don_num, don_sup)
                        return don_inf, don_num, don_sup
                    elif t_val == "duo":
                        (lineno(), "RETURN duo", duo, "f_val, f_pos", f_val, f_pos)
                        return f_val, f_pos
                    break


    ("# Avec le dictionnaire des valeurs individualisées par clé."
     "il est indispensable de réunir ce qui peut l'être :"
     "      Joindre les tétras autres que ceux de la clé du rassemblement à d'autres rassemblements.")
    cop_val = valeurs.copy()
    tous_1234 = []  # Tetras déjà visités
    dict_tet = {}  # Dico du reconstitutionnement
    mem_clone = []  # Cette liste mémorise les clones
    for duo in t_double.keys():
        # Créer une copie de valeurs[duo]
        ("\n", lineno(), "DUO", duo, "valeurs[duo]", valeurs[duo])
        cop_val[duo] = valeurs[duo].copy()
        don_inf, don_sup, don_num = "", "", ""
        dict_tet[duo] = []
        "# Commencer par réunir les clones en tête du groupement des tétras."
        for val in cop_val[duo]:
            if val[0] == t_double[duo]:
                "# Tétra cloné"
                if val[0] not in tous_1234:
                    tous_1234.append(val[0])  # Val[0] = Nom de la gamme.
                retour_t = go_inf("duo", duo, val[1])
                for rt in retour_t:
                    if len(rt) > 1:
                        for it in rt:
                            if "inf" in it:
                                don_inf = it[:len(it)-3]
                                (lineno(), "don_inf", don_inf)
                            elif "sup" in it:
                                don_sup = it[:len(it) - 3]
                                (lineno(), "don_sup", don_sup)
                    if retour_t[0].isnumeric():
                        don_num = retour_t[0]
                        (lineno(), "NUM rt", rt, "retour_t[0]", retour_t[0], retour_t)

                dict_tet[duo] =[(don_inf, don_num, don_sup)]

                "# Vérification de l'aspect de clonage du tétra inf et du tétra sup dans chaque gamme."
                mem_clone.append(retour_t)
                (lineno(), "mem_clone", mem_clone)
                # 201 mem_clone [('1234000005678', ['1234inf', '1234sup']), ('1200340560078', ['120034inf',
                # '120034sup']), ('1020340506078', ['102034inf', '102034sup']), ('1002340500678',
                # ['100234inf', '100234sup'])]


                (lineno(), "duo", duo, "* Clone val[0]", val[0], "dict_tet", dict_tet[duo])
                # 191 duo 1234 * Clone val[0] o45x dict_tet [('1234', '1234000005678', '1234')]
                break  # Éviter la répétition
                # Sans le break = 198 duo 1234 * Clone val[0] o45x dict_tet [('1234', '1234000005678', '1234')]
                # 198 duo 1234 * Clone val[0] o45x dict_tet [('1234', '1234000005678', '1234')]
                # Avec le break = 198 duo 1234 * Clone val[0] o45x dict_tet [('1234', '1234000005678', '1234')]

        "# Recommencer la lecture de cop_val"
        for val in cop_val[duo]:
            if val[0] not in tous_1234:
                retour_t = go_inf("dia", duo, val[1])
                (lineno(), "val[1]", val, "retour_t", retour_t)
                # 199 val[1] ('o46-', '1234000560078', 'inf') retour_t ('1234', '1234000560078', '120034')
                if retour_t not in dict_tet[duo]:
                    dict_tet[duo].append(retour_t)
                    (lineno(), "*-\t duo", duo, "*", retour_t)
                    # 180 *-	 duo 1234 * ('1234000005678', ['1234inf', '1234sup'])
        # 82 duo 1234 o45x valeurs [('o45x', '1234000005678', 'inf'), ('o45x', '1234000005678', 'sup')...]
        # break  # Premier essai d'une seule tranche tétracordique en mode clone.

    ("# Comment poursuivre la série des tétras sans se répéter ?"
     "  - Créer une liste de clefs à visiter en ordre.")
    t_visio = []  # Liste les clés qui n'ont pas été utilisées
    for k_glob in k_global:
        if k_glob not in t_double.keys():
            t_visio.append(k_glob)
    ("\n", lineno(), "t_visio", t_visio, "\n valeurs", valeurs)
    # 214 t_visio ['1002034', '10002034', '100002034', '12304', '123004', '12034', ...]
    # valeurs {'1234': [('o45x', '1234000005678', 'inf'), ('o45x', '1234000005678', 'sup')...] ...}

    "# Continuer à compléter le dictionnaire dict_tet, dans lequel se rangent les éclaircissements."
    for k_vis in t_visio:
        if k_vis not in dict_tet.keys():
            dict_tet[k_vis] = []
        val_t = valeurs[k_vis].copy()
        (lineno(), "k_vis", k_vis, "val_t", val_t)
        # 224 k_vis 10000234 val_t [('^2', '1000023456078', 'inf')]
        for vt in val_t:
            retour_t = go_inf("dia", k_vis, vt[1])
            (lineno(), "vt", vt, "retour_t", retour_t)
            # 228 vt ('o45-', '1234005006078', 'sup') retour_t ('1234', '1234005006078', '100234')
            # 228 vt ('^2', '1000023456078', 'inf') retour_t ('100234', '1000023456078', '12034') ERREUR
            if retour_t not in dict_tet[k_vis]:
                dict_tet[k_vis].append(retour_t)
                (lineno(), "*-\t k_vis", k_vis, "*", retour_t)
                # 218 *-	 k_vis 1002034 * ('1234', '1234005006078', '100234')
            (lineno(), "k_vis", k_vis, "vt", vt)
            # 210 k_vis 1002034 vt ('o45-', '1234005006078', 'sup')
        (lineno(), "k_vis", k_vis, "dict_tet", dict_tet[k_vis])
        # 214 dict_tet [('100234', '1002345006078', '1002034')]

    def diatonic(tet1, dia1_t, dia2_t, tet2, gam_t):
        """Fonction de vérification diatonique du tétra par rapport à l'original
        ,   dia1_t = Le développement diatonique du tétra-clef du dictionnaire principal
        ,   diat2_t = Le deuxième élément du couple tétra complémentaire"""
        (lineno(), "Def diatonic, tet1&dia12_t&tet2", tet1, dia1_t, dia2_t, tet2, "gam_t", gam_t)
        # 263 Def diatonic, tet1&dia12_t&tet2 1234 ['0000', '0000', '0000', '0000'] 0000 1234
        # gam_t ('1234', '1234000005678', '1234')

        "# Relevé diatonique de l'élément couplé à la clé tétra."
        dia_tet2, a2 = [], tet2
        for i in range(len(a2)):
            rotation = a2[i:] + a2[:i]
            if rotation[0] != "0":
                ima_rotate = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), rotation))
                dia_tet2.append(ima_rotate)
        (lineno(), "tet2", tet2, "dia_tet2", dia_tet2)
        # 264 tet2 12034 dia_tet2 ['00-00', '0-000', '0000-', '000-0']

        "# Inversion du tétra original et clé du programme."
        un_envers = dia1_t[0][::-1]
        de_nul, de_deg = 0, ""
        for ue in un_envers:
            if ue == "0":
                de_nul += 1
                de_deg += str(de_nul)
            else:
                de_deg += "0"
        (lineno(), "tet1", tet1, dia1_t[0], "Degrés inversés", de_deg, "un_envers", un_envers)
        # 285 tet1 102034 0-0-00 Degrés inversés 120304 un_envers 00-0-0


        "# Dictionnaire à remplir : 315 dict_miroir_org dict_keys(['miror', 'clone', 'juxta', 'symet', 'diato'])"
        dia_un, dia_deux, dia_ego = 0, 0, False  # Les degrés de chacune des diatonies
        rapport_dia = []  # Le lien des degrés diatoniques
        for un in dia1_t:  # Consultation de la liste diatonique
            if dia_un == 4:
                dia_un = 0
            dia_un += 1

            "# Vérification de l'aspect symétrique de chacun des tétras entrants et des diatonies."
            if tet1 not in copie_tet:
                copie_tet.append(tet1)
                long_t = len(un)
                # Trouver l'axe du milieu du tétra. Vide ou non, il est égal à lui-même.
                axe_t = long_t // 2
                if dia1_t.count(dia1_t[0]) == 1:
                    sym0, deg1 = False, 0
                    for ind1 in dia1_t:
                        deb1, fin1, sym1 = 0, -1, 0
                        deg1 += 1  # Degré concerné par la symétrie
                        while deb1 + 1 <= axe_t:
                            if ind1[deb1] == ind1[fin1]:
                                sym1 += 1
                                (lineno(), "Test iso", ind1, deb1, fin1, sym1, "ind_fin1", ind1[deb1], ind1[fin1])
                                # 288 Test iso 00--00 0 -1 1 ind_fin1 0 0
                            deb1 += 1
                            fin1 -= 1
                            if sym1 == axe_t:
                                sym0 = True
                                (lineno(), "Symétrie", ind1, "deg1", deg1)
                                # 295 Symétrie 00--00 deg1 1
                                break
                        if sym0:
                            if tet1 not in dict_miroir_org['symet'].keys():
                                dict_miroir_org['symet'][tet1] = (ind1, deg1)
                                (lineno(), "dict_miroir_org['symet'][tet1]", dict_miroir_org['symet'][tet1])
                                # 310 dict_miroir_org['symet'][tet1] ('00--00', 1)
                            break
                    (lineno(), tet1, un, "long_t", long_t, "axe_t", axe_t, dia1_t)
                    # 304 120034 00--00 long_t 6 axe_t 3 ['00--00', '0--000', '0000--', '000--0']

            "# Liste des degrés romains : deg_rom"
            for deux in dia_tet2:
                if dia_deux == 4:
                    dia_deux = 0
                dia_deux += 1
                deg1_t, deg2_t = deg_rom[dia_un - 1], deg_rom[dia_deux - 1]

                "# Quand les longueurs des deux tétras du couple sont identiques."
                if len(un) == len(deux):
                    dia_ego = True
                    ("# Pendant que les tétras ont les mêmes longueurs, on peut estimer :"
                     "      Le miroitage par le renversement tétra."
                     "      Le clonage par la répétition du tétra."
                     "      La diatonie par la modulation des tétras.")
                    # L'effet miroir entre le tétra infarieur et le tétra supérieur.
                    # La similitude entre le tétra inférieur et le tétra supérieur.
                    # La familiarité diatonique entre le tétra infarieur et le tétra supérieur.

                    "# Chercher les tétras clones_inf/sup diatoniques dans la liste mem_clone"
                    if un == deux:
                        rapport_dia = tet1, deg1_t, tet2, deg2_t, gam_t
                        "# Les deux tétras inf/sup sont similaires."
                        for mc in mem_clone:
                            if tet1 in mc[1][0] and tet1 == tet2:
                                if tet1 not in dict_miroir_org["clone"].keys():
                                    dict_miroir_org["clone"][tet1] = [rapport_dia]
                                elif rapport_dia not in dict_miroir_org["clone"][tet1]:
                                    dict_miroir_org["clone"][tet1].append(rapport_dia)
                                dict_miroir = dict_miroir_org["clone"][tet1]
                                (lineno(), "2=1, \tdict_miroir_org['clone']", tet1, dict_miroir)
                                # 346 2=1, 	dict_miroir_org['clone'] 1234 [('1234', 'I', '1234', 'I')]

                    "# Trouver les tétras qui miroitent les tétras originaux, d'une même longueur."
                    # un_envers = un[::-1]
                    if un_envers == deux and tet2 == de_deg:
                        rapport_dia = tet1, deg1_t, tet2, deg2_t, gam_t
                        if tet1 not in dict_miroir_org["miror"].keys():
                            dict_miroir_org["miror"][tet1] = [rapport_dia]
                        elif rapport_dia not in dict_miroir_org["miror"][tet1]:
                            dict_miroir_org["miror"][tet1].append(rapport_dia)
                        dict_miroir = dict_miroir_org["miror"][tet1]
                        (lineno(), "2=1, \tdict_miroir_org['miror']", tet1, dict_miroir)
                        # 371 2=1, 	dict_miroir_org['miror'] 1234 [('1234', 'I', '1234', 'I',
                        # ('1234', '1234000005678', '1234'))]
                        (lineno(), "un_envers et deux", un_envers, deux, "\t rapport", rapport_dia, gam_t)
                        (lineno(), "tet1", tet1, dia1_t[0], "Degrés inversés", de_deg, "un_envers", un_envers)
                        # 366 tet1 102034 0-0-00 Degrés inversés 120304 un_envers 00-0-0

                "# Le tétra clé du couple est dans la liste diatonique du complément tétra"
                if un in deux:  # Le tétra clé du couple est dans la liste diatonique du complément tétra
                    # Est-ce que les deux tétras comparés ont le même nombre de caractères ?
                    if dia_ego is False:  # Quand les longueurs des deux tétras du couple sont différents.
                        len_un, len_deux = len(un), len(deux)
                        rapport_dia = tet1, len_un, deg1_t, tet2, len_deux, deg2_t, gam_t
                        dict_miroir_org["juxta"][tet1] = rapport_dia
                        (lineno(), "2!=1, \t<<<<\tdict_miroir_org['juxta'][tet1]", dict_miroir_org["juxta"][tet1])
                        # 340 2!=1, 	<<<<	dict_miroir_org['juxta'][tet1] ('1234', 4, 'I', '120034', 6, 'III')
                    else:
                        rapport_dia = tet1, deg1_t, tet2, deg2_t, gam_t
                        "# Si le premier tétra est inclus dans la diatonie du deuxième tétra = 1 diatonic à 2"
                        dict_miroir_org["diato"][tet1] = rapport_dia
                        (lineno(), "2=1, \tdict_miroir_org['diato'][tet1]", dict_miroir_org["diato"][tet1])
                        # 346 2==1, 	dict_miroir_org['diato'][tet1] ('1234', 'I', '1234', 'I')
                    return un
                "# Le tétra complémentaire est dans la liste diatonique de la clé tétra"
                if deux in un:  # Le tétra complémentaire est dans la liste diatonique de la clé tétra
                    # Est-ce que les deux tétras comparés ont le même nombre de caractères ?
                    if dia_ego is False:  # Quand les longueurs des deux tétras du couple sont différents.
                        len_un, len_deux = len(un), len(deux)
                        rapport_dia = tet1, len_un, deg1_t, tet2, len_deux, deg2_t, gam_t
                        dict_miroir_org["juxta"][tet1] = rapport_dia
                        (lineno(), "2!=1, \t<<<<\tdict_miroir_org['juxta'][tet1]", dict_miroir_org["juxta"][tet1])
                        # 356 2!=1, 	<<<<	dict_miroir_org['juxta'][tet1] ('120034', 6, 'III', '1234', 4, 'I')
                    else:
                        rapport_dia = tet1, dia_1, tet2, dia2, gam_t
                        "# Si le deuxième tétra est inclus dans la diatonie du permier tétra = 2 diatonic à 1"
                        dict_miroir_org["diato"][tet1] = rapport_dia
                        (lineno(), "2==1, \tdict_miroir_org['diato'][tet1]", dict_miroir_org["diato"][tet1])
                        # La ligne 362 ne s'est jamais affichée.
                    return deux

    ("# Visualiser toutes les composantes du dictionnaire : dict_tet."
     "v_noms[k_glob].append(val1)  # Dico, clé = tétra et valeur = nom de la gamme")
    k_ = list(dict_tet.keys())
    copie_tet = []  # Mémorisation des tétras originaux pour le traitement de la symétrisation.
    quantetra_lis = []  #, quantetra_lis = liste des quantités
    quantetra_key = k_.copy()  #, quantetra_key = liste des clefs tétras
    '''dict_miroir_org = {
        "miror" : {},  # Le tétra devant un miroir à effet symétrique
        "clone" : {},  # Le tétra se répète à l'identique. Voir: mem_clone[liste], ligne 200
        "juxta": {},  # Le tétra se répète à l'identique dans une autre échelle[len(tétra)]
        "symet" : {},  # Le tétra est symétrique à lui-même, ligne 309
        "diato": {},  # Le tétra est diatonique à l'original, ligne 344
    }  # Dico, clef = tétra et valeur = couple tétra aux valeurs symétriques.'''
    (lineno(), "dict_miroir_org", dict_miroir_org.keys())
    # 380 dict_miroir_org dict_keys(['miror', 'clone', 'juxta', 'symet', 'diato'])
    for k in k_:
        quantetra_lis.append(len(dict_tet[k]))  #, q_lis = liste des quantités.E
        (lineno(), "k", k, "dict_tet", dict_tet[k], len(dict_tet[k]))
        # 264 k 10000234 dict_tet [('100234', '1000023456078', '12034')] 1
        ("\n", lineno(), "Clef tétra k référence sélection.", k)
        # 314 Clef tétra k référence sélection. 1234
        ("# Traitement de l'image tétra. Exemple : "
         "data = ['203040', '000000', '123456']"
         "resultat = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), data))")
        # Former l'image de la clé et son inverse
        k_cop = k  # L'image de la clé[k_cop]
        k_rec = list(k_cop)
        k_rec.reverse()
        k_ver = "".join(str(x) for x in k_rec)  # L'image de la clé inverée[k_ver]
        # Transmutation ['102034'] en ['0-0-00'], pour une forme basique exploitable[k_ver]
        ima_recto = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), k_cop))
        ima_verso = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), k_ver))
        (lineno(), "k", k, "k_cop", k_cop, ima_recto, "k_ver", k_ver, ima_verso)
        # 263 k 120034 k_cop 120034 00--00 k_ver 430021 00--00

        "# Relevé diatonique de la clé tétra."
        dia_tet, a = [], k_cop
        for i in range(len(a)):
            rotation = a[i:] + a[:i]
            if rotation[0] != "0":
                ima_rotate = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), rotation))
                dia_tet.append(ima_rotate)
        (lineno(), "dia_tet", dia_tet)
        # 271 dia_tet ['00--00', '0--000', '0000--', '000--0']

        "# Il faut vérifier qu'ima2_retro n'est pas diatonique à k_cop."
        ima2_recto, ima3, deg_rom = "", "", ["I", "II", "III", "IV"]
        if len(dict_tet[k]) == 1:
            dtk = dict_tet[k]
            (lineno(), "Clé k", k, "k_cop", k_cop, "=  dtk[0][0]", dtk[0][0])
            # 305 Clé k 100002034 k_cop 100002034 =  dtk[0][0] 1234
            if dtk[0][0] != k_cop:  # Renvoie l'élément du couple de k
                ima3 = dtk[0][0]
                ima2_recto = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), ima3))
            else:
                ima3 = dtk[0][2]
                ima2_recto = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), ima3))
            retour_tet = diatonic(k_cop, dia_tet, ima2_recto, ima3, dtk[0])
            if retour_tet:
                (lineno(), "Mono_Clé k", k, ">  dtk", dtk, "\tretour_tet", retour_tet, ima3)
                # 355 Mono_Clé k 12300004 >  dtk [('12300004', '1230000456078', '12034')] 	retour_tet 0000- 12034
        else:
            for dtk in dict_tet[k]:
                if dtk[0] != k_cop:
                    ima3 = dtk[0]
                    ima2_recto = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), ima3))
                else:
                    ima3 = dtk[2]
                    ima2_recto = ''.join(map(lambda x: ''.join(['-' if c == '0' else '0' for c in x]), ima3))
                (lineno(), "k", k, ">  dtk", dtk, "ima2_recto", ima2_recto)
                # 279 k 1234 >  dtk ('1234', '1234000005678', '1234') ima2_recto 0000
                retour_tet = diatonic(k_cop, dia_tet, ima2_recto, ima3, dtk)
                if retour_tet:
                    (lineno(), "Multi_Clé k", k, "=  dtk", dtk, "\tretour_tet", retour_tet, ima3)
                    # 368 Multi_Clé k 1234 =  dtk ('1234', '1234000005678', '1234') 	retour_tet 0000 1234
        # break  # Traitement de la première clef tétra uniquement

    (lineno(), "dict_tet", dict_tet, len(k_))
    # 444 dict_tet {'1234': [('1234', '1234000005678', '1234'), ('1234', '1234000560078', '120034')...]} 28
    "# 380 dict_miroir_org dict_keys(['miror', 'clone', 'juxta', 'symet', 'diato'])"
    for dmo in dict_miroir_org.keys():
        (lineno(), "dmo", dmo, dict_miroir_org[dmo])

    ("# Création d'un dictionnaire dont la clé est la quantité des gammes réunies et la valeur sont les tétras."
     "Quand il y a plusieurs fois une même quantité, on crée des repères indiquants le fait, le reste n'est pas fait."
     "  En utilisant :"
     "      , quantetra_ord : commence par les plus grosses entités"
     "      , quantetra_lis : classement original de la liste des quantités"
     "      , quantetra_key : classement original des clés de la liste tétra"
     "      , quant_suite   : liste de suivi pour les quantités en doublon")
    quantetra_dic = {}  # , quantetra_dic = dico, clef = tetra, valeur = liste des tétras.
    quantetra_ord = quantetra_lis.copy()  #, quantetra_lis = liste des quantités.
    quantetra_ord.sort()  # , q_ord est trié en ordre croissant.
    quantetra_ord.reverse()  # ' q_ord est inversé, il commence par les plus grosses entités.
    (lineno(), "Les quantités\t", quantetra_ord, "\n\t\t\t\t\t", quantetra_lis)
    # 260 Les quantités  [18, 17, 12, 12, 11, 11, 7, 5, 5, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # 					 [17, 11, 18, 11, 7, 4, 1, 2, 5, 12, 1, 1, 3, 12, 1, 3, 5, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1]
    quant_suite = []
    for qtt in quantetra_ord:
        if quantetra_ord.count(qtt) == 1:
            ind_qtt = quantetra_lis.index(qtt)
            quantetra_dic[quantetra_key[ind_qtt]] = dict_tet[quantetra_key[ind_qtt]]
            (lineno(), "qtt", qtt, "ind_qtt", ind_qtt, "quantetra_dic", quantetra_dic[quantetra_key[ind_qtt]])
            # 244 qtt 18 ind_qtt 2 quantetra_dic [('102034', '1020340506078', '102034')...]
        else:
            cnt = -1
            for c_qtt in quantetra_lis:
                cnt += 1
                if qtt == c_qtt and quantetra_key[cnt] not in quant_suite:
                    quant_suite.append(quantetra_key[cnt])
                    quantetra_dic[quantetra_key[cnt]] = dict_tet[quantetra_key[cnt]]
                    (lineno(), cnt, "Q", qtt, c_qtt, "dict_tet", dict_tet[quantetra_key[cnt]][0])
                    break
    ("\n", lineno(), "quantetra_dic", quantetra_dic, len(quantetra_dic.keys()))
    # 256 quantetra_dic {'102034': [('102034', '1020340506078', '102034')...]} 28

    ("# Assimilation des liaisons entre les tétras (inversions incluses)."
     "Clarification par absence des doublons, une avancée constructive interrelationnelle.")
    dict_relate_org = {}  # Dico, clef = tétra et valeur = couple tétra, selon l'organisation originale.
    dict_relate_ord = {}  # Dico, clef = tétra et valeur = couple tétra, selon l'organisation ordonnée.

    "# Assemblage des deux dictionnaires pour obtenir deux dimensions des liaisons tétras."
    select_ord = list(dict_tet.keys()), list(quantetra_dic.keys())

    "# Lecture de la liste contenant les deux dictionnaires"
    cnt_dic = 0
    for so in select_ord:
        k_ = so
        list_memore, k1_, k2_ = [], [], []  # Liste des couples déjà visités et variables poncteuelles.
        # Lecture de dict_tet pour assembler les duos tétracordiques des gammes primordiales.
        for clef in k_:
            dict_relate_org[clef] = []  # Déclaration de la clef tétra utile.
            dict_relate_ord[clef] = []  # Déclaration de la clef tétra utile.
            k1 = dict_tet[clef]
            if len(k1) > 1:
                for k2 in k1:
                    k2_ = [k2[0], k2[2]]
                    k2r = k2_.copy()
                    k2r.reverse()
                    if k2_ not in list_memore and k2r not in list_memore:
                        list_memore.append(k2_)
                        if cnt_dic == 0:
                            dict_relate_org[clef].append(k2_)
                        else:
                            dict_relate_ord[clef].append(k2_)
                (lineno(), "clef", clef, "dict_relate_org", dict_relate_org[clef], "\t", len(dict_relate_org[clef]))
                # 242 clef 1234 dict_relate_org [['1234', '1234'], ['1234', '120034'], ['1234', '102034']...]  15
            else:
                k1_ = [k1[0][0], k1[0][2]]
                k1r = k1_.copy()
                if k1_ not in list_memore and k1r not in list_memore:
                    list_memore.append(k1_)
                    if cnt_dic == 0:
                        dict_relate_org[clef].append(k1_)
                        dro = dict_relate_org[clef]
                        (lineno(), "clef", clef, "dict_relate_org", dro, "\t", len(dro))
                        # 250 clef 12300004 dict_relate_org [['100234', '12034']] 	 1
                    else:
                        dict_relate_ord[clef].append(k1_)

            if cnt_dic == 0:
                if dict_relate_org[clef]:
                    (lineno(), "dict_relate_org", dict_relate_org[clef], "\t", len(dict_relate_org[clef]))
                else:
                    del dict_relate_org[clef]
            else:
                if dict_relate_ord[clef]:
                    (lineno(), "dict_relate_ord", dict_relate_ord[clef], "\t", len(dict_relate_ord[clef]))
                else:
                    del dict_relate_ord[clef]
        if cnt_dic == 0:
            ("\n", lineno(), "dict_relate_org", dict_relate_org, len(dict_relate_org.keys()))
            # 351 quantetra_dic {'1234': [['1234', '1234'], ['1234', '120034'], ['1234', '102034']} 28
        else:
            ("\n", lineno(), "dict_relate_ord", dict_relate_ord, len(dict_relate_ord.keys()))
            # 354 quantetra_dic {'1234': [['1234', '1234'], ['1234', '120034'], ['1234', '102034']} 28
        cnt_dic += 1

    "# Inventaire des acquis"
    ("   Tétras total = union {'1234': '1234', '12304': '12304', '123004': '123004', ...] 28"
     "   Tétras communs = ponton {'1234': '1234', '12034': '12034', '120034': '120034', ...] 9"
     "   Tétras supérieurs uniques = super {'1002034': '1002034', '10002034': '10002034', ...] 5"
     "   Tétras inférieurs uniques = infer {'12304': '12304', '123004': '123004', ...] 14"
     "# Dictionnaires des liaisons inter-tétracordiques"
     "   Dico : dict_relate_org, ordonnance originale"
     "   Dico : dict_relate_ord, ordonnance ordonnée"
     "# Dictionnaire des positions internes au tétras"
     "   Dico : dic_tet_maj 102034 ([0, 0, 0, 0], [1, 3, 5, 6], 6)")

    "# Organisation et utilitaires :"
