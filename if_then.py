choise = 'ham'
dict = {
    'spam': 1.25, # Инструкция ‘switch’ на базе словаря
    'ham': 1.99, # Используйте has_key или get для
    'eggs': 0.99, # значения по умолчанию
    'bacon': 1.10}

#print(dict[choise])

branch = {
    'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99
}

#print(branch.get('spam', 'bad choise'))
#print(branch.get('bacon', 'bad choise'))

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)

# A = Y if X else Z - интересная особенность языка
# X = A or default - можно присваивать таким образом, это позволит сэкономить

# if f1() or f2(): ... - удобно, если нужно выполнить две проверки подряд
# если первая None, вторая выполняется






