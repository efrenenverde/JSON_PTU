from pokemonLoop import pokemonLoop

pokemon = {}
currentPokemonArray = []
ignoredUpper =['HP:', 'TM', 'M', 'F', '(N),']

with open("DATA/testDex.txt", "r") as f:
    for line in f:
        for word in line.split():
            if word.isupper() and word not in ignoredUpper:
                print(currentPokemonArray)
                currPokemon = pokemonLoop(currentPokemonArray)
                currPokemon.setStuff(currentPokemonArray)
                currentPokemonArray = []
                currentPokemonArray.append(word)
            else:
                currentPokemonArray.append(word)
