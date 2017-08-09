print('Задача 1: Основы')
def basic(x):
    print(x)
basic('Строка')
basic(10)

print('Задача 2: Аргументы')
def adder(x, y):
    return x + y
print(adder(1,2))
print(adder('строка', 'другая строка'))
print(adder(['список','первый'], ['список', 2]))

print('Задача 3: Переменное число аргументов')
def adder1(*args):
    print('adder1', end=' ')
    if type(args[0]) == type(0):
        sum = 0
    else:
        sum = args[0][:0]
    for arg in args:
        sum = sum + arg
    return sum
print(adder1(1))
print(adder1([1, 30], [2, 3]))

print('Задача 4: Именованные аргументы')
def adder2(**kwargs):
    print('adder2', end=' ')
    spisok = []
    for key in kwargs.keys():
        spisok.append(kwargs.get(key))
    if isinstance(spisok[0], (int, float)):
        sum = 0
    else:
        sum = spisok[0][:0]
    for item in spisok:
        sum += item
    return sum
print(adder2(good=[323, 23], bad=['dfsf', 2]))
print(adder2(g=1, f=2, l=9))

print('Задача 5: копируем словарь')
def copyDict(dict):
    newdict = dict.copy()
    newdict['l'] = 'это новый словарь'
    return newdict
olddict = {
    'Бомжиха' : 'тупая',
    'Бомж' : 'вонючий'
}
print(copyDict(olddict))
print(olddict)

print('Задача 6: объединение двух словарей')
def addDict(dict1, dict2):
    if isinstance(dict1, dict):
        dict1.update(dict2)
    else:
        return dict1 + dict2
dict1 = {
    'Бомжиха' : 'тупая',
    'Бомж' : 'вонючий'
}
dict2 = {
    1: 2,
    3: 5
}
addDict(dict1, dict2)
print(dict1)
print(addDict([3, 5], [ 2,1]))

print('Задача 7: сопостовляем аргументы')
# ничего осбенного

print('Задача 8: простые числа')
def simple(y):
    x = y // 2
    if y % x == 0:
        print(y, 'has factor', x)
        print(float(y), 'has factor', x)
        return
    else:
        print(y, 'is prime')
        print(float(y), 'is prime')
        return
simple(14)

print('Задача 9: генераторы спискоты')
import math
L = [2, 4, 9, 16, 25]
a = (list(math.sqrt(x) for x in L))
b = (list(map(math.sqrt, L)))
newL = []
for item in L:
    newL.append(math.sqrt(item))
print(newL)

print('Задача 10: хронометраж')
# потом