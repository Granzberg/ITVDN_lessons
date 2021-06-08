import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

for person_data in root:
    print('PK: ', (person_data.attrib, person_data.get('pk')))
    element1 = getattr(person_data.find('./first_name'), 'text', None)
    element2 = getattr(person_data.find('./last_name'), 'text', None)
    element3 = getattr(person_data.find('./age'), 'text', None)
    print('{} {} {}'.format(element1, element2, element3))

first_names = root.findall('./person/first_name')
last_names = root.findall('./person/last_name')
ages = root.findall('./person/age')

print('*'*75)
for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

print('*'*75)

for person_data in root:
    print('PK: ', person_data.attrib)
    for worker in person_data:
        print('{} {}'.format(worker.tag, worker.text))
print('*'*75)
