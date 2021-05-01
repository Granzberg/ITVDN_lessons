args = int(input("Введите числовые аргументы: "))
args = map(int, str(args))
args = list(args)
print(args)


def my_average(number):
    the_sum = 0
    for _ in number:
        the_sum = the_sum + _

    x = len(number)
    the_sum = the_sum / x
    return the_sum


def arg(numbers):
    return float(sum(numbers))/len(numbers)


print(my_average(args))

print(arg(args))

