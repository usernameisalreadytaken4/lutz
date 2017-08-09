def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights()
print(act('robin'))

title = 'Sir'
act = lambda x: title + ' ' + x
print(act('robin'))

import sys

snowall = lambda x: list(map(sys.stdout.write, x))

t = snowall(['spam\n', 'toast\n', 'eggs\n'])

showall = lambda x: [sys.stdout.write(line) for line in x]

t = showall(('bright\t', 'side\t', 'of\t', 'life\n'))


counters = [1, 2, 3, 4]
def inc(x):
    return x + 10

print(list(map(inc, counters)))
print(list(map((lambda x: x + 3), counters)))
