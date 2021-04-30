args = int(input("Введите числовые аргументы: "))
args = map(int, str(args))
args = list(args)
print(args)


def my_average(*numb):
    the_sum = 0
    for _ in numb:
        the_sum = the_sum + _

    x = len(numb)
    the_sum = the_sum / x
    return the_sum


def arg(*numb):
    return sum(numb)/len(numb)


print(my_average(args))

print(arg(args))
print(arg(*range(15)))
