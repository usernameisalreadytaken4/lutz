#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.last_name())
print(sue.last_name())
sue.give_raise(.10)
print(sue.pay)