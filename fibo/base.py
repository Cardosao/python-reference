#!/usr/bin/env python3


def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=', ')
    while ultimo <= limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=', ')


def fibo_list(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


def fibo_list2(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


def fibo_list_qtd(qtd):
    resultado = [0, 1]
    while len(resultado) < qtd:
        resultado.append(sum(resultado[-2:]))
    return resultado


def fibo_list_qtd2(qtd):
    resultado = [0, 1]
    for _ in range(2, qtd):
        resultado.append(sum(resultado[-2:]))
    return resultado


def fibo_list_recursive(qtd, sequencia=(0, 1)):
    if len(sequencia) == qtd:
        return sequencia
    return fibo_ternario(qtd, sequencia + (sum(sequencia[-2:]),))


def fibo_ternario(qtd, sequencia=(0, 1)):
    return sequencia if len(sequencia) == qtd else \
        fibo_ternario(qtd, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    fibonacci(20000)
    print('')
    for item in fibo_list(10000):
        print(f'{item}', end=', ')
    print('')
    for item in fibo_list2(10000):
        print(f'{item}', end=', ')
    print('')
    for item in fibo_list_qtd(10):
        print(f'{item}', end=', ')
    print('')
    for item in fibo_list_qtd2(10):
        print(f'{item}', end=', ')
    print('')
    for item in fibo_list_recursive(10):
        print(f'{item}', end=', ')
    print('')
    for item in fibo_ternario(10):
        print(f'{item}', end=', ')
    print('')
