# coding: utf-8

from random import randint

first_names = ["Valentin", "Melanie", "Mathilde"]
last_names = ["Bark", "Four", "Quick"]


def get_random_name(names):
    random_index = randint(0, 2)
    return names[random_index]


print(get_random_name(first_names))

freelancer = {
    "first_name": get_random_name(first_names),
    "last_name": get_random_name(last_names)
}


generate_freelancer_requested = input(
    'Voulez vous générer un freelance ? [Y/n]') or 'Y'

if generate_freelancer_requested not in ['y', 'n']:
    print("La commande n'existe pas")

if generate_freelancer_requested == "y":
    print(freelancer)
elif generate_freelancer_requested == "n":
    print("On ne te connais pas")
else:
    print('Commande inconnu')
