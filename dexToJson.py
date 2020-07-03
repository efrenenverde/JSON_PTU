from system import pokemonLoop
import os

currentPokemonArray = []
ignoredUpper =['HP:', 'Y', 'X', 'TM', 'M', 'F', '(N),', '(N)', '(A)', 'X-',
 'U-', '(F)', '(M)', '(G)', 'MIME', 'NULL', 'KOKO', 'FINI', 'LELE', 'BULU', 'RKS', 'RIME']
ignoredFirstLoop = False

dexTxtFile = ["DATA/Gen7 copy.txt"]
targetFile = "data.txt"

# TODO: Pumpkaboo and Gourgheist are thicc bicc's ( Fix their Stat List )

try:
    os.remove(targetFile)
except IOError:
    print('File not accesible')

currNumber = 0

for document in dexTxtFile:
    with open(document, "r") as f:
        for line in f:
            for word in line.split():
                if word.isupper() and word not in ignoredUpper:
                    if ignoredFirstLoop:
                        currNumber = currNumber + 1
                        currPokemon = pokemonLoop.PokemonLoop(currentPokemonArray, currNumber)
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
finalTxt = open("finalJson.txt", "wt")

finalTxt.write('{"species":\n[')

for line in rawTxt:
	finalTxt.write(line.replace('}}}][{"_id":', '}}},\n{"_id":')[1:-1])

finalTxt.write(']}')

rawTxt.close()
finalTxt.close()

print('Done!')