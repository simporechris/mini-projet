import pytest
from solution import calculer_taxe


#Fred
#Arrange
@pytest.mark.parametrize("produits_choisi","sous_total","resultat_attendu", [
    (["biscuit", "fromage", "jus d'orange" ], 8.50, 9.77)
])
def test_code1(produits_choisi,sous_total,resultat_attendu):
    #Act
    resultat = calculer_taxe(sous_total,produits_choisi)
    #Assert
    assert isinstance(resultat, float)
    assert resultat == resultat_attendu