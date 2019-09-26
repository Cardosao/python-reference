#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import urllib.request


def execute(url):
    with urllib.request.urlopen(url) as entrada:
        print('Baixando arquivo...')
        dados = entrada.read().decode('latin1')
        print('Download completo')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')
        entrada.close()

    if not entrada.read():
        print('\nArquivo já foi fechado!')


if __name__ == '__main__':
    execute(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
