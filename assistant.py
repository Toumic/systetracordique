# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module assistant.py

def assiste(objet):
    """L'assistant aide à informer discrètement sur le sujet des modules"""
    prefixes = ('(', '#', '"#', '("', '("#')

    with open(objet, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            if ligne.strip().startswith(prefixes):
                print(ligne.strip())


if __name__ == '__main__':
    assise = ["systetra.py", "globaliste.py", "tetravisuel.py"]
    assiste(assise[0])
