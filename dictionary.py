pidors = {
    'Вася Пупкин': 'Натурал',
    'Николай Петрович': 'Пидор',
    'Петр Николаевич': 'Натурал',
    'Игорь Сидорович': 'Пидор'
}


def generator(value):
    for man in pidors:
        if pidors.get(man) == value:
            yield man
'''
print('Натуралы:')
for i in generator('Натурал'):
    print(i)

print('Пидоры:')
for i in generator('Пидор'):
    print(i)
'''

A = generator('Пидор')

# print(A.__next__())
# print(A.__next__())
B = pidors.items()
for i in B:
    print(i[1])
print(pidors.items())