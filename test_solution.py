import pytest
from solution import calculer_taxe, calculer_reduction


#chris
@pytest.mark.parametrize("produits_choisi,sous_total,resultat_attendu", [
    (["biscuit", "fromage", "jus d'orange" ], 8.50, (0.43,0.85,9.78))
])
def test_solution1(produits_choisi,sous_total,resultat_attendu):
    #Act
    resultat = calculer_taxe(sous_total,produits_choisi)
    #Assert
    assert resultat == resultat_attendu

#fatoumata
@pytest.mark.parametrize("produits_choisi,sous_total,resultat_attendu", [
    (["polar-pop", "pain", "chips" ], 3.89, (0.19,0.39,4.47))
])
def test_solution2(produits_choisi,sous_total,resultat_attendu):
    #Act
    resultat = calculer_taxe(sous_total,produits_choisi)
    #Assert
    assert resultat == resultat_attendu
#Fred
@pytest.mark.parametrize("produit_choisi,produit_disponible,resultat_attendu")
    
liste_produits_rab = ["biscuit", "lait", "pain"]
    rabais_pfixe = [1.60, 0.99, 0.80]
def test_calculer_reduction(produit_choisi,produit_disponible)
    #act
    resultat = calculer_reduction(produit_choisi,produit_disponible)
    #assert
    assert resultat == resultat_attendu
