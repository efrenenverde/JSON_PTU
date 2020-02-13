import pokemonLoop
import os

currentPokemonArray = []
ignoredUpper =['HP:', 'Y', 'X', 'TM', 'M', 'F', '(N),', '(N)', '(A)', 'X-',
 'U-', '(F)', '(M)', '(G)', 'MIME', 'NULL', 'KOKO', 'FINI', 'LELE', 'BULU', 'RKS']
ignoredFirstLoop = False

with open("DATA/Gen7.txt", "r") as f:
    os.remove("data.txt")
    for line in f:
        for word in line.split():
            if word.isupper() and word not in ignoredUpper:
                if ignoredFirstLoop:
                    currPokemon = pokemonLoop.PokemonLoop(currentPokemonArray)
                    currPokemon.resetAll()
                    currPokemon.setAll()
                    currPokemon.toArray()

                ignoredFirstLoop = True
                currentPokemonArray = []
                currentPokemonArray.append(word)
            else:
                currentPokemonArray.append(word)
