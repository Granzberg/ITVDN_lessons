class ReversedList(object):
    def __init__(self, my_list=[]):
        self.my_list = my_list

    def __getitem__(self, index):
        if 0 >= index > 3:
            return my_list.index(index)


my_list = [1, 2, 5, 7, 32, 148]
print(my_list.index(5))
'''
my_list = list(reversed(my_list))
print(my_list)
'''
iter = ReversedList()

print(iter(my_list))

