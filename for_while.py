print('Пример 1: выводим список циклом')
for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')

print('Пример 2: присваиваем кортежи')
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:  # Операция присваивания кортежа в действии
    print(a, b)

print('Пример 3: смотрим элементы словарей')
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

print(list(D.items()))

for (key, value) in D.items():
    print(key, '=>', value)

print('Пример 4:  вот что мы делаем, когда нам нужны параллельные итерации')
L1 = [1,2,3,4]
L2 = [5,6,7,8]
for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)

print('Пример 5: составляем словарь из двух списков с помощью итерации')
keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]

print(list(zip(keys, vals)))
D2 = {}
for (k, v) in zip(keys, vals):
    D2[k] = v # можно апдейтить словарь так
print(D2)

# или самая мякотка, можно сделать так:
D3 = dict(zip(keys, vals))
print(D3)

print('Пример 6: enumerate, или как нахуй послать каунты, что я раньше использовал')
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)
# почему? да патамушта enumerate - генератор
E = enumerate(S)
print(next(E))
print(next(E))