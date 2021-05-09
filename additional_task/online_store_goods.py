from store import Goods
import pickle

pen = Goods('pen', 10)
book = Goods('book', 1000)
notebook = Goods('notebook', 100)
Goods.make_sets(pen, notebook)

with open('Lesson_8_task0.pkl', 'wb') as data:
    pickle.dump((pen, notebook), data)


