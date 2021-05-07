'''
n = int(input("n = "))
lst = [2]

for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            lst.append(num)
            break

print(lst)
'''

for num in range(2, 101):
    if all(num % i != 0 for i in range(2, num)):
       print(num)
