def definir_prix(prix_total):
        for key, value in produit.items():
                prix_total = key * value

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
nom = produit.keys()
prix = produit.values()
for key, value in produit.items():
        print(f"{key} : {value}$")
prix = definir_prix()

#todo:faire des reductions pour les produits speciaux
#Todo pour Fred: cree la fonction reduction
#todo pour fatoumata:cree pour la fonction pour la taxe
#todo si on a le temps: vente d'essence
