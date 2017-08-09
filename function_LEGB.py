def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)
print(f(3))
q = maker(3)
print(q(4))
# это можно использовать для многократного доступа к разным частям базы данных

def make_actions():
    acts = []
    for i in range(5):
        # acts.append(lambda x: i ** x) - так не работает
        acts.append(lambda x, i=i: i ** x)
    return acts

acts = make_actions()
print(acts[0](2))
print(acts[2](2))


def tester(start):
    state = start

    def nested(label):
        nonlocal state # nonlocal позволяет проводить операции с переменной выше
        print(label, state)
        state += 1
    return nested

F = tester(0)
print(F('spam'))
print(F('ham'))
print(F('eggs'))