"""
fonction definir_prix
    définir nom du produit
    définir le prix
    rétouner None
creation dictionnaire de produit et des prix


fonction calculer_taxe
    calculer le tps
    calculer le tvq
    calculer le prix total
    retourner le tps, le tvq et le prix total


fonction Calculer_réduction(produits_client)
#Fred
def calculer_reduction(produits_client):

liste_produits_rab:liste des produits dans le circulaire de rabais accessible aux clients

   liste_produits_rab = ["biscuit","lait","pain"]

rabais_pfixe:liste de prix réduits pour les cirulaires qui vont remplacer les prix initiaux

   rabais_pfixe=[1.60,0.99,0.80]

sujet à changements

    pour chaque prod dans produits_client:
       si prod dans liste_produits_rab:
          nouveau_prix = rabais_pfixe[prod]
           ls_prix[prod] = nouveau_prix


   retourner ls_prix



fonction supprimer_produit(produits_client)
    Tant que c'est vrai
        Demandez à l'utilisateur d'entrez le nom du produit
        si l'utilisateur tape Entrer
            finsi
        si le nom du produit est dans la liste des produits choisi
            supprimer le produit
            affichez le nom du produit supprimé
        sinon
            afficher vous n'avez pas choisi ce produit




programme principal

"""

"""
    EXEMPLE D'EXECUTION
=================================        
        Nom du depanneur
          Reçu client
        Adresse
=================================
date : 20/10/2025 13:41:10
biscuit             2.20$
fromage             3.50$
jus d'orange        2.80$
----------------
Sous-Total :        8.50$
Tps :               0.43$
Tvq :               0.85$
Total :             9.78$
----------------------------------------
Nombre total d'articles: 3
----------------------------------------
Ventes finales sur tous les articles

    Merci d'avooir magasiner chez nous!
        Passer une belle journée.


"""