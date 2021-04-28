def reverse(my_list):
    for index in range(len(my_list)-1, -1, -1):
        yield my_list[index]


for char in reverse([1, 2, 3, 4, 5, 6]):
    print(char)
