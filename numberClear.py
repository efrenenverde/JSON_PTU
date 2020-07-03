import os

class getNumberDictionary:
    numTxt = open("DATA/pokeNumberList.txt", "r")

    numberDictionary = []
    numberDictionary2 = []

    for line in numTxt:
        split = line.split()
        numberDictionary.append({split[1]: split[0]})
        numberDictionary2.append({'name':split[1].upper(),'number': split[0]})

    numTxt.close()

    def getNumberDictionary(self):
        return self.numberDictionary

    def getNumber(self, specie):
        for x in self.numberDictionary2:
            if x['name'] == specie:
                return (x['number'])
        
        print(specie + ' number not found')
            
c = getNumberDictionary()

c.getNumber('BULBASAUR')