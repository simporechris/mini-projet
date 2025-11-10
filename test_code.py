import pytest
import code as test_code

#Fred
#Arrange
@pytest.mark.parametrize("produits_choisi","sous_total","prix_total", [
    (["biscuit", "fromage", "jus d'orange" ], 8.50, 9.77)
])

#Act
#Assert
#assert resultat == resultat_attendu