# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
id1 = my_list.pop(1)
id2 = my_list.pop(3)
my_list.insert(1, id2)
my_list.insert(3, id1)
print(my_list)