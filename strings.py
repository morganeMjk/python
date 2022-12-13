my_text1= """Texte
multiligne
abc
foo
bar"""
print(my_text1)

my_text2= "Texte\nmultiligne\nabc\nfoo\nbar"
print(my_text2)

# interpolation avec un f-string
my_number1 = 123
my_text3 = f"Nombre = {my_number1}"
print(my_text3)

my_text4 = f"""
Le nombre
est
{my_number1}
foo
"""
print(my_text4)

# afficher des acolades dans une heredoc f-string
my_text5 = f"""
{{
foo
}}
{{bar}}
"""
print(my_text5)

# concatenation
my_number2 = 3.14
my_text6 = "Le nombre PI est " + str(my_number2)
print(my_text6)

# tronquer un float dans une interpolation f"texte {variable:.nombreDécimalef}"
my_number3 = 1 / 3
my_text7 = f"1 / 3 ~= {my_number3:.4f}"
print(my_text7)

# les interpolations acceptent les expressions
my_text8 = f"1 + 1 = {1 + 1}"
print(my_text8)

# définition d'une fonction utilisateur
# écriture de documentation pour une fonction
def hello(name : str) -> None:
    """Cette fonction dit bonjour à quelqu'un

    name str indique le nom de la personne à saluer
    return None
    """
    print(f"Salut {name}")
# appel d'une fonction
hello('Toto')
# appeler la documentation d'une fonction avec help(hello)

# longueur d'un str
my_text9 = "Lorem ipsum dolor sit amet ipsum consectetur adipisicing elit."
my_number4 = len(my_text9)
print(my_number4)

# trouver la position d'un mot dans un str
# 0123456
# lorem ipsum
my_number5 = my_text9.find('ipsum')
print(my_number5)
my_number5 = my_text9.find('ipsum' , my_number5 + 1)
print(my_number5)

# compter le nombre d'occurence dans un str
my_number6 = my_text9.count('ipsum')
print(my_number6)

# remplacer du texte dans un str - la variable d'origine n'est pas changée, seul le resultat est mdofié
print(my_text9.replace('Lorem' , 'Foo'))
# pour modifier la valeur de la variable définitivement il faut réaffecter une nouvelle valeur à la variable
my_text9 = my_text9.replace('Lorem' , 'Foo')
print(my_text9)

# transformer un str en liste
my_list1 = my_text9.split()
print(my_list1)
print(len(my_list1))

# afficher le premier caractère d'une liste
print(my_text9[0])

# affichage du 0e au 10e caractère d'une liste
print(my_text9[0:10])
print(my_text9[:10])

# affichage du 10e au dernier caractère d'une liste
print(my_text9[10:])

# affichage les éléments d'une liste à partir du dernier
print(my_text9[::-1])