#!/usr/bin/env python3


def get_dia(dia):
    dias = {
        1: 'Dom',
        2: 'Seg',
        3: 'Ter',
        4: 'Qua',
        5: 'Qui',
        6: 'Sex',
        7: 'Sab',
    }
    return dias.get(dia, "** inválido **")


PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}
textos = [' Joao gosta de futebol e politica',
          'A praia foi divertida']

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado: ', texto)

if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia(dia)}')
