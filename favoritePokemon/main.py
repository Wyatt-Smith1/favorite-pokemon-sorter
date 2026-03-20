import math
import random

from allpokemon import pokemon


# Runs Pokemon up the list until it is worse than one
def sort_pokemon_v1(poke, favs):
    ind = 0

    if len(favs) == 0:
        favs.append(poke)
        return

    while ind < len(favs):
        choice = input(f'Which Pokemon is better: 1. {poke}, 2. {favs[ind]} ')
        if choice == '1':
            ind += 1
        elif choice == '2':
            favs.insert(ind, poke)
            return
        else:
            print('Please type 1 or 2 to make your choice')


# Uses binary sort to place Pokemon
def bin_sort_pokemon(poke, favs):
    if len(favs) == 0:
        favs.append(poke)
        return

    discovered = [False] * len(favs)
    ind = math.floor((len(favs))/2)
    hi = len(favs)
    lo = 0

    while True:
        choice = input(f'Which Pokemon is better: 1. {poke}, 2. {favs[ind]} ')
        discovered[ind] = True
        if choice == '1':
            prev = ind
            lo = ind
            halfway = (lo+hi)/2
            ind = math.floor(halfway)
        elif choice == '2':
            prev = ind
            hi = ind
            halfway = (lo+hi)/2
            ind = math.floor(halfway)
        else:
            print('Please type 1 or 2 to make your choice')
            continue

        if discovered[ind]:
            offset = 1 if choice == '1' else 0
            favs.insert(prev+offset, poke)
            return


favorites = []
pokemon_rand = pokemon.copy()
random.shuffle(pokemon_rand)

for pokemon in pokemon_rand:
    bin_sort_pokemon(pokemon, favorites)
    print(favorites)

print(f'Here is every Pokemon sorted from you least- to most-favorite: {favorites}')
