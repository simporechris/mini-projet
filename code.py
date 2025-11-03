import datetime
from datetime import *


def definir_prix(prix_total):
    nom = produit.keys()
    prix = produit.values()

#todo fatoumata:cree pour la fonction pour la taxe
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


#todo:faire des reductions pour les produits speciaux
#Todo pour Fred: cree la fonction reduction
#todo si on a le temps: vente d'essence




if __name__ == "__main__":
    print("=="*20)
    print("           Dépanneur GO!  ")
    print("            Reçu client")
    date = datetime.today()
    print(f"date : {(date.strftime("%m/%d/%Y  %H:%M:%S"))}")
    produits_choisi = ["lait", "barre chocolatée", "biscuit" ]
    for items in produits_choisi:
        print(f"{items:<20}          {produit[items]: .2f}$")
    print("--"*20)

    print("--" * 10)
    print("Ventes finales sur tous les article du dépaneur GO!")
    print("      Merci de magasiner chez! \n      Passez une belle journée.")



