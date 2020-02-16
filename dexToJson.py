from system import pokemonLoop
import os

currentPokemonArray = []
ignoredUpper =['HP:', 'Y', 'X', 'TM', 'M', 'F', '(N),', '(N)', '(A)', 'X-',
 'U-', '(F)', '(M)', '(G)', 'MIME', 'NULL', 'KOKO', 'FINI', 'LELE', 'BULU', 'RKS', 'RIME']
ignoredFirstLoop = False

dexTxtFile = ["DATA/Gen7.txt", "DATA/GalarDex.txt"]
targetFile = "data.txt"

# TODO: Pumpkaboo and Gourgheist are thicc bicc's ( Fix their Stat List )

try:
    os.remove(targetFile)
except IOError:
    print('File not accesible')

for document in dexTxtFile:
    with open(document, "r") as f:
        for line in f:
            for word in line.split():
                if word.isupper() and word not in ignoredUpper:
                    if ignoredFirstLoop:
                        currPokemon = pokemonLoop.PokemonLoop(currentPokemonArray)
                        currPokemon.resetAll()
                        currPokemon.setAll()
                        currPokemon.toJson()

                    ignoredFirstLoop = True
                    currentPokemonArray = []
                    currentPokemonArray.append(word)
                else:
                    currentPokemonArray.append(word)

f.close

rawTxt = open(targetFile, "rt")
finalTxt = open("out.txt", "wt")

for line in rawTxt:
	finalTxt.write(line.replace('}}][{"_id": ', '}}{"_id": ')[1:-1])

rawTxt.close()
finalTxt.close()

print('Done!')