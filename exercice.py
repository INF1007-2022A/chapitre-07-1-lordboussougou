#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici

#4
def quatre_a(chaine1):
    set1 = {'a', 'c', 'g', 't'}
    chaine2 = set(chaine1)
    return chaine2.issubset(set1)

def quatre_b():
    while True:
        chaine = input("Veuillez saisr une chaine ADN : ")
        if quatre_a(chaine):
            break

def proportion(chaine, seq):
    return (len(seq)*chaine.count(seq) /len(chaine) )*100



# TODO: Appelez vos fonctions ici

chaine = "attgcaatggtggtacatg"
séquence = "ca"
p = proportion(chaine,séquence)
print(f"Il y a {p:2f} % de {séquence}.")



