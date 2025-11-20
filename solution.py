import datetime
from datetime import *


def definir_prix(produits_choisi, nom_produit):  #Chris
    """
    fonction pour calculer le sous total
    :param produits_choisi: les produits choisis par le clients
    :param nom_produit: Les noms de produits
    :param prix: Le prix de chaque produit
    :return: None
    """
    nom_produit = produit.keys()
    prix = produit.values()
    return None
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
#todo fatoumata:cree pour la fonction pour la taxe
def calculer_taxe(sous_total,produits_choisi):#fatoumata
    """
    fonction pour calculer les taxes après le sous total
    :param sous_total: le sous total est le prix total avant les taxes
    :return: le tps, le tvq et le prix total de la facture
    """

    tps = round(sous_total * 0.05,2)
    tvq = round(sous_total * 0.099975,2)
    prix_total = sous_total +tps + tvq
    return tps, tvq, prix_total




#todo:faire des reductions pour les produits speciaux
#Todo pour Fred: cree la fonction reduction
#Fred
def calculer_reduction(produits_client, produits_disponibles):
    """
    Applique des rabais fixes sur certains produits.
    """
    liste_produits_rab = ["biscuit", "lait", "pain"]
    rabais_pfixe = [1.60, 0.99, 0.80]

    produits_avec_reduc = produits_disponibles.copy()
    for i, prod in enumerate(liste_produits_rab):
        if prod in produits_client:
            produits_avec_reduc[prod] = rabais_pfixe[i]
    return produits_avec_reduc

def supprime_produit(produits_choisi): #chris
    while True:
        item = input("* ")
        if item == "":
            break

        if item in produits_choisi:
            produits_choisi.remove(item)
            print(f" {item} a été supprimé")
        else:
            print(f"{item} cela ne fait pas partie de vos produits")



if __name__ == "__main__":  # chris et fatoumata
    produits_choisi = []
    print("Entrez vos produits (Taper 'Entrer' pour terminer)")
    while True:
        item = input("- ").lower()
        if item == "":
            break
        produits_choisi.append(item)

    print("Écrivez le nom du produit à supprimer ou taper 'Entrer' pour terminer")
    supprime_produit(produits_choisi)


    print("=="*20)
    print("           Dépanneur GO!  ")
    print("            Reçu client\n")
    print("     101 Rue Mckenzie,Chibougamau,\n           Québec, G8P 2G6\n            418 654-2121")
    print("--" * 20)
    date = datetime.today()
    print(f"date : {date.strftime('%m/%d/%Y, %H:%M:%S')}")

    ls_prix = []
    try:
        for items in produits_choisi:
            ls_prix.append(produit[items])
            print(f"{items:<20}          {produit[items]: .2f}$")
    except KeyError:
        print(f" {items} n'existe pas dans notre dépanneur")

    print("--" * 10)
    sous_total = definir_prix(produits_choisi, produit)

    sous_total = sum(ls_prix)
    print(f"Sous-total :{sous_total:>23.2f}$")
    tps, tvq, prix_total = calculer_taxe(sous_total,produits_choisi)
    print(f"TPS(5%) : {tps:>25.2f}$")
    print(f"TVQ(9.975%) : {tvq:>21.2f}$")
    print(f"Total : {prix_total:>27.2f}$")
    print("--" * 20)
    nb_article= len(produits_choisi)
    print(f"Nombre total d'articles: {nb_article}")



    #afficher reçu
    print("--" * 20)
    print("Ventes finales sur tous les articles\n ")

    print("   Merci de magasiner chez nous! \n     Passez une belle journée.")




