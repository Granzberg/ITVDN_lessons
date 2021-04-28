class ReverseList:

    def __init__(self, my_list):
        self.my_list = my_list
        self.index = len(my_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.my_list[self.index]


rev = ReverseList([1, 2, 3, 4, 5, 6])

for char in rev:
    print(char)
my_list01 = [1, 2, 3, 4, 5, 6]
print("*"*15)
for i in my_list01:
    print(i)
