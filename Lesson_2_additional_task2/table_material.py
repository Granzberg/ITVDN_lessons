import json

table = {
        'id': 'id',
        'weight': 'weight',
        'height': 'height',
        'material_characteristics': ('char',('characteristic', 'value')),
        }


data = json.dumps(table)
for element in table:
    print(element)
print(data)
