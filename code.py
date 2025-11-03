from pydoc import source_synopsis


def definir_prix(prix_total):
    nom = produit.keys()
    prix = produit.values()


def calculer_taxe(prix_total, taux_taxe):
    sous_total = float(input("f"))
    tps = sous_total * 0.05
    tvq = sous_total * 0.099975
    prix_total = sous_total +tps + tvq
    return prix_total

produit = {
        "eau": 1.20,
        "coca-cola": 2.50,
        "chips": 1.80,
        "sandwich jambon-beurre": 3.90,
        "barre chocolatée": 1.50,
        "café": 1.00,
        "lait": 1.30,
        "pain": 1.10,
        "biscuit": 2.20,
        "fromage": 3.50,
        "jus d'orange": 2.80,
        "pomme": 0.80,
        "banane": 0.70,
        "yaourt": 1.10,
        "cigarettes": 9.50,
        "polar-pop": 0.99
}
for key, value in produit.items():
    print(f"{key} : {value}$")


#todo:faire des reductions pour les produits speciaux
#Todo pour Fred: cree la fonction reduction
#todo :cree pour la fonction pour la taxe
#todo si on a le temps: vente d'essence
