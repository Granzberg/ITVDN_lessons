import csv

quoting = csv.QUOTE_ALL

with open('data.csv', 'w') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['id', 'weight', 'height', 'material_characteristics'],
        quoting=quoting
    )
    writer.writeheader()

    writer.writerow({
        'id': '1',
        'weight': 20,
        'height': 50,
        'material_characteristics': ('char', ('characteristic', 'value'), ('value', 'value')),
    })

