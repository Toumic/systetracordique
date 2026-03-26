# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Module tetravisuel : Ce module traite les clés et les contenus du dictionnaire systetra.t_global

# from tkinter import *
import inspect
from typing import Callable

# lino() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


def affiche_tetra():
    """Cette fonction du module affiche les positions des tétracordes après les tris."""
    print("\n", lineno(), "*** MODULE - tetravisuel.py")
