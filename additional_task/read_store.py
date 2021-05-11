import json
import pickle

with open('Lesson_8_task0.pkl', 'rb') as data:
    goods = pickle.load(data)
    str(goods)
    print(goods)
with open('Lesson_8_task0.json', 'w') as data2:
    data2.write(" ".join(str(x) for x in goods))
    data2.close()
    data.close()
print(data2)
