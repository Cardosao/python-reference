#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('../pessoas.csv') as arquivo:
    with open('../pessoas.output.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome {}, Idade {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print('Arquivo já foi fechado!')
if saida.closed:
    print('Saida já foi fechado!')
