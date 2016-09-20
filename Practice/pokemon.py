# A program that tells you what starter pokemon you have chosen

def your_starter_pokemon():
    import random
    pokemons = ['Bulbasaur!', 'Squirtle!', 'Charmander!']
    pokemon = pokemons
    if pokemon is pokemons:
           print "Your starter pokemon is", random.choice(pokemons)
    elif pokemon is 'Unknown':
        print "You don't have any starter pokemons!"
your_starter_pokemon()
