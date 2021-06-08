import csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "*"
    delimiter = "!"
    lineterminator = '\n'


class CustomDialect1(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "~"
    delimiter = "$"
    lineterminator = '\n'


csv.register_dialect('tester', CustomDialect)
csv.register_dialect('tester1', CustomDialect1)


with open('data.csv', 'w+') as file:
    writer = csv.writer(file, dialect='tester')
    #writer = csv.writer(file, dialect='tester1')
    writer.writerow(["1", "9000", "lasdadasj", "ldkadsadsa"])
    writer.writerow(["1", "9000", "lasdadasj", "ldkadsadsa"])
    writer.writerow(["1", "9000", "lasdadasj", "ldkadsadsa"])
    writer.writerow(["1", "9000", "lasdadasj", "ldkadsadsa"])
    writer.writerow(["1", "9000", "lasdadasj", "ldkadsadsa"])
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)



