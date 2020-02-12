import json

class pokemonLoop:
    SpeciesName = ''
    InfoArray = []

def __init__(self, Name="there", Data=['empty']):
    self.SpeciesName = Name
    self.InfoArray = Data

def toArray(self):
    species = {}
    species[self.SpeciesName] = []
    species[self.SpecieesName].append({
        'id': self.SpeciesName

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