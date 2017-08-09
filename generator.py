res = [x + y for x in [0, 1 , 2] for y in [100, 200, 300]]
print(res)

res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res)


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

print(list(mymap(abs, [-2, -1, 0, 1, 2])))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))

print(list(mymap(abs, [-2, -1, 0, 1, 2])))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


def myzip(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

print(list(myzip('abc', 'lmnop')))