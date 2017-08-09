print('Задача 1(a): ')
S = 'джигурда'
print(list(ord(i) for i in S))

print('Задача 1(b):')
S = 'джигурда'
print(sum(list(ord(i) for i in S)))

print('Задача 1(c):')
S = 'джигурда'
L = [ord(i) for i in S]
print(L)
# ЧСХ, код ниже практически идентичен, только возвращает объект map
# это говорит о том, что вариант ниже лучше для работы, а выше - для вывода
L = map(ord, S)
print(L)


print('Задача 2:')
for i in range(2):
    print('hello %d\n\a' % i)
# ничего не произошло


print('Задача 3:')
D = {
    'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99
}
print(sorted(vals for vals in D.values()))


print('Задача 4:')
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = 1
    else:
        i = i+1
if found:
    print('at index', i)
else:
    print(X, 'not found')

print('Задача 4(a):')
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = 1
        break
    else:
        i = i+1
else:
    print(X, 'not found')
print('at index', i)

print('Задача 4(b):')
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
for i in L:
    if 2**X == i:
        break
else:
    print(X, 'not found')
print('at index', L.index(i))

print('Задача 4(c):')
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
result = 2**X in L
print(result)

print('Задача 5(c):')
L = []
for i in range(X):
    L.append(2**i)
print(L)

print('Задача 5(e):')
X = 5
L = [2**X for i in range(X)]
