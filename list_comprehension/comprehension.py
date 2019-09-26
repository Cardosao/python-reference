#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def get_list():
    dobros = [i ** 2 for i in range(1000) if i % 2 == 0]
    print(f'List: Uso de memoria: {sys.getsizeof(dobros)}')
    for value in dobros:
        print(value, end=' ')


def get_generators():
    dobros = (i ** 2 for i in range(1000) if i % 2 == 0)
    print(f'Gen: Uso de memoria: {sys.getsizeof(dobros)}')
    for i in dobros:
        print(i, end=' ')


def get_dict():
    dobros = {i: i ** 2 for i in range(1000) if i % 2 == 0}
    print(f'Dict: Uso de memoria: {sys.getsizeof(dobros)}')
    for chave, valor in dobros.items():
        print(f'{chave}: {valor}', end=' ')


if __name__ == '__main__':
    get_list()
    print()
    get_generators()
    print()
    get_dict()

