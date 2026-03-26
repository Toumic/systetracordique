# Organisation tétracordique

Le système gammique comporte soixante-six principales gammes. <br>
Chaque gamme est composée de deux tétracordes. <br>

Combien de tétracordes allons-nous trouver  ?

### HISTOIRE DE L'ALGORITHME    

Le travail se fait avec la liste des soixante-six gammes fondamentales (k_gam), elle est basée sur un seul type de 
classement, alors qu'il existe deux types de classements de ces gammes. La liste ne comporte que des formes énumérées,
comme par l'exemple de la gamme naturelle : C_D_EF_G_A_BC ⇒ 1020340506078.

En un premier temps, (k_gam), a été perçue comme possédant deux tétracordes chacune. Une seule gamme a deux tétras,
l'un est en position inférieure`['12304']` et l'autre en position supérieure`['50678']`. Les positions aident à 
produire les deux séries tétras enregistrés dans les listes (`t_inf['12304'], t_sup['10234']`).

La liste des gammes primordiales énumérées : `k_gam = [('o45x', '123400000567'), ('o46-', '123400056007'),`.

Ensuite, les listes de positionnement des tétras, servent à renseigner le dictionnaire général (t_global). Ce dico 
a des clés sous forme tétra et les valeurs associées représentent les chronologies topographies :
`# t_global['1234'] | '1234': ['o45x.1234000005678.inf', 'o45x.1234000005678.sup'`.

Le dico t_global sera utilisé après l'analyse des listes tétras : `t_inf, t_sup = [], []  # Listes : tétras[inf, sup].`.

#### LISTE DES GAMMES ÉNUMÉRÉES : e_gam = [e for _, e in k_gam]
Cette liste : e_gam, contient les gammes énumérées et elle va servir au traitement de la séparation des tétras.
La série `t_inf` comporte vingt-trois [23] éléments et celle de `t_sup`, en a quatorze [14], ces deux niveaux peuvent 
avoir des similitudes. Postopération d'enregistrement de la série des tétras sans doublon, consigne dans le dico t_global
vingt-huit [28] éléments tétracordiques parmi les gammes. <br>
_________________________________________________________
###### SÉRIALISATION DES CONJONCTURES
Nous avons une topographie des tétras (inférieurs, supérieurs, communs, union).

* **Les tétras inférieurs sont au nombre de vingt-trois.**
* **Il y a quatorze tétras inférieurs uniques.**
* **Les tétras supérieurs sont au nombre de quatorze.**
* **Il y a cinq tétras supérieurs uniques.**
* **Il y a neuf tétras communs à ceux des inférieurs et ceux des supérieurs.**
* **Vingt-huit tétracordes composent les utilités musicales.**

**Il y a plusieurs contextes à afficher, les sérialisations et les liens nominaux.** <br>


# U
prefixes = ("def", "class", "#", "import")

with open("mon_script.py", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        if ligne.strip().startswith(prefixes):
            print(ligne.strip())
