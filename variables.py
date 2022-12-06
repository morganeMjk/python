# l'opérateur d'affectation  = permet d'injecter une valeur dans une variable


# integer (nombre entier)

my_number1 = 123
my_number2 = -42
print(type(my_number1))
print(my_number2)

# chaine de caractère (string)

my_text1 = 'ceci est une chaine de caractère'
my_text2 = "ceci est aussi une chaine de caractère"
print(type(my_text1))
print(my_text2)

# saut de ligne

my_text3 = "abc\ndef\nghi"
print(my_text3)

# ou

my_text4 = """abc
def
ghi"""
print(my_text4)

# float (nombre à virgule flottante)

my_number3 = 3.14
my_number4 = -2.71
my_number5 = 0.0

print(my_number3)
print(my_number4)
print(my_number5)

# booleans

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# valeur nulle (none)

my_none = None
print(my_none)
print(type(None))

# permutation de la valeur des variables
a = 123
b = 42
a, b = b, a
print(a, b)

a = 123
b = 42
c = a
a = b
b = c
print(a, b)

a = 123
b = 42
c = a + b
a = c - a
b = c - b
print(a, b)


# transtypage
foo = "123"
foo = int(foo)
print(type(foo))

