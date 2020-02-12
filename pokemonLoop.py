import json

class pokemonLoop:
    SpeciesName = ''
    InfoArray = []
    Capabilities = []

    def __init__(self, Data=['empty']):
        self.SpeciesName = Data[0]
        self.InfoArray = Data

    def setStuff(self, Data=['Empty']):
        for i in range(self.InfoArray.size):
            print(self.InfoArray.size, i)

    def toArray(self):

        species = {}
        species[self.SpeciesName] = []
        species[self.SpeciesName].append({
            '_id': self.SpeciesName

        })



data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)