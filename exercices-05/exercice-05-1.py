# exo 5.1
# Ajoutez de la documentation à la fonction suivante et vérifiez
# qu'elle s'affiche correctement en utilisant la fonction help()

# réponse 5.1
def multiplication(a: float, b: float) -> float:
    """Cette fonction multiplie la valeur de la variable a par celle de la variable b
    
    a float indique un nombre décimal
    b float indique un nombre décimal
    return float
    """
    return a * b

help(multiplication)