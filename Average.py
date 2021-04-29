args = int(input("Введите числовые аргументы: "))
args = map(int, str(args))
args = list(args)


def my_average(args):
    the_sum = 0
    for _ in args:
        the_sum = the_sum + _

    x = len(args)
    the_sum = the_sum / x
    return the_sum


print(my_average(args))
