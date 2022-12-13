fruits = ['ananas', 'banane', 'cerise']
print(fruits)

# afficher l'élément d'une liste
print(fruits[0])

# affecter l'élément d'une liste a une variable
my_fruit = fruits[0]
print(my_fruit)

# remplacer un élément d'une liste
fruits[0] = 'abricot'
print(fruits)

# afficher l'élément d'un liste à partir d'une variable
my_count = len(fruits)
index = 0
if index < my_count:
    print(f'{index = }')
    print(fruits[index])
index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])
index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])
index += 1
if index < my_count:
    print(f'{index = }')
    print(fruits[index])

# ajouter un élément
fruits.append('datte')
print(fruits)

# supprimer un élément
del fruits[2]
print(fruits)



fruits = ['ananas', 'banane', 'cerise', 'datte']

# supprime et renvoie le dernier élément
last_element = fruits.pop()
print(fruits)
print(last_element)

# supprime et renvoie le premier élément
first_element = fruits.pop(0)
print(fruits)
print(first_element)

# insérer un élément
fruits.insert(1, 'kiwi')
print(fruits)