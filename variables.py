# l'opérateur d'affectation  = permet d'injecter une valeur dans une variable


# integer (nombre entier)

my_number1 = 123
my_number2 = -42

# chaine de caractère (string)

my_text1 = 'ceci est une chaine de caractère'
my_text2 = "ceci est aussi une chaine de caractère"

# saut de ligne

my_text3 = "abc\ndef\nghi"

# ou

my_text4 = """abc
def
ghi"""

# float (nombre à virgule flottante)

my_number3 = 3.14
my_number4 = -2.71
my_number5 = 0.0

# booleans

my_boolean1 = True
my_boolean2 = False

# valeur nulle (none)

my_none = None

# permutation de la valeur des variables
a = 123
b = 42
a, b = b, a

a = 123
b = 42
c = a
a = b
b = c

a = 123
b = 42
c = a + b
a = c - a
b = c - b

# transtypage (type casting)
foo = "123"
foo = int(foo)

# un chiffre transformé en bool renverra True, sauf 0 qui renvoie False
my_number6 = 10

# opérateur d'inclusion
fruits = ['ananas', 'banane', 'cerise']

result = 'ananas' in fruits
print(result)
result = 'fraise' in fruits
print(result)

if fruits:
    print('La liste contient des éléments')
else:
    print('La liste ne contient aucun élément')








