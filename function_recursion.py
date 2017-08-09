def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5]))


def mysum2(L):
    return 0 if not L else L[0] + mysum(L[1:])


def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])


def mysum4(L):
    first, *rest = L # проверка на наличие
    return first if not rest else first + mysum(rest)

# рекурсия полезна для обхода вложенных списков (страница 541)

