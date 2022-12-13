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