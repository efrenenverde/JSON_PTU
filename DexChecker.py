import json

with open('speciesData.json') as json_file:
    data = json.load(json_file)
    for p in data['species']:
        for mo in p['Evolution']:
            if mo[3] != "Null":
                print('Name: ' + p['_id'])
                print(mo)