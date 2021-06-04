import json

data = {
    'loading': [{
        'first_name': 'Eugene',
        'last_name': 'Petrov',
        'age': 35,
        'hobbies': [
            'guitar',
            'cars',
            'mountains',
            'adventures',
        ]
    },
    {
        'first_name': 'Max',
        'last_name': 'Anperov',
        'age': 33,
        'hobbies': [
            'cars',
            'adventures',
        ]
    }]
}
with open('output.json', 'w') as f:
    json.dump(data, f)
    f.close()


with open('output.json', 'r') as r:
    loading = json.load(r)
    r.close()
    print(loading)

