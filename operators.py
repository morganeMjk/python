# importer une librairie Random et Math
import random
import math

#  = affectation
foo = 123

# + addition
foo = 123 + 42

# += incrémentation (++ n'existe pas en python)
foo += 42

# - soustraction
foo = 123 - 42

# -= décrémentation (-- n'existe pas en python)
foo -= 42

# / division
foo = 123 / 42

# // division entière
foo = 123 // 42

# % modulo
foo = 4 % 3
foo = random.randint(1,100)

# * multiplication
foo = 123 * 42

# ** puissance
# ^ puissance mais pas en python
foo = 2 ** 2

# math.sqrt() racine carré
foo = math.sqrt(4)
foo = 4 ** 0.5
foo = 4 ** (1/2)

# ** (1/3) racine cubique
foo = 8 ** (1/3)


# les opérateurs de comparaison

# == égalité (différent de === qui vérifie la valeur ET le type, n'existe pas en python)
result = 1 == 1

# opérateurs de grandeur
result = 123 < 42

result = 123 >= 42

# != inégalité
result = 123 != 42

# les encadrements
my_number = random.randint(0, 100)
result = 0 <=  my_number < 50

result = "abc" < "bcd"

# opérateur AND (le print sera Vrai s'il n'y a aucune condition Fausse)
result = True and False
result = False and True
result = True and True
result = False and False

a = random.randint(0,1)
b = random.randint(0,1)
result = a and b

# opérateur OR (le print sera Vrai s'il y a au moins une condition Vrai)
result = True or False
result = False or True
result = True or True
result = False or False

# not opérateur de négation
result = not True
result = not False

