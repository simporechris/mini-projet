import pytest
import code as test_code
from code import calculer_taxe


#Fred
#Arrange
@pytest.mark.parametrize("produits_choisi","sous_total","prix_total","resultat attentu", [
    (["biscuit", "fromage", "jus d'orange" ], 8.50, 9.77)
])
def test_code1(produits_choisi,sous_total,prix_total):


#Act
resultat = calculer_taxe()
#Assert
resultat_attendu = 9.77
assert resultat == resultat_attendu