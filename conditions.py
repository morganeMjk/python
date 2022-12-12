import random


if True:
    print("La conditions est vraie")
    print("Ce code est exécuté")

if False:
    print("La condition est fausse")
    print("Ce code n'est pas exécuté")


conditions_vente = False
if conditions_vente:
    print("L'utilisateur a accepté les conditions de vente")
else:
    print("L'utilisateur n'a pas accepté les conditions de vente")

if not conditions_vente:
    print("L'utilisateur n'a pas accepté les conditions de vente")
else:
    print("L'utilisateur a accepté les conditions de vente")


emails = random.randint(0,3)
if emails == 1:
    print("Vous avez un nouveau mail")
elif emails > 1:
    print(f"Vous avez {emails} nouveaux mails")
else:
    print("Vous n'avez pas de nouveaux mails")


windows_closed = bool(random.randint(0, 1))
electricity_off = bool(random.randint(0, 1))
print(f'{windows_closed = }')
print(f'{electricity_off = }')
if windows_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print("l'électricité est coupée")
elif not windows_closed and electricity_off:
    print("Les fenêtres ne sont pas fermées")
    print("l'électricité est coupée")
elif not electricity_off  and windows_closed:
    print("Les fenêtres sont fermées")
    print("l'électricité n'est pas coupée")
else:
    print("Les fenêtres ne sont pas fermées")
    print("l'électricité n'est pas coupée")


bank_card = True
cash = True

if bank_card or cash:
    print("On a un moyen de paiement")
    if bank_card:
        print("On a la carte bancaire")
    if cash:
        print("On a du liquide")
else:
    print("On a aucun moyen de paiement")


ticket = True
vip = False
registration = False
print(f'{ticket = }')
print(f'{vip = }')
print(f'{registration = }')
if (ticket or vip) and registration:
    print('Access authorized')
else:
    print('Access not authorized')


product_count = random.randint(0, 50)
if product_count > 20:
    print('Il y a plus de 20 articles')
    print('RAS')
elif 5 < product_count <= 20:
    print('Il y a plus de 5 articles')
    print('Alerte approvisionnement')
elif 0 < product_count <= 5:
    print('Il y a plus de 0 articles')
    print('Alerte rupture imminente')
else:
    print("Il n'y a plus d'article")
    print('Alerte rupture')