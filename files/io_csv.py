#!/usr/bin/env python
# -*- coding: latin1 -*-
import csv
import requests


def execute(url):
    with requests.get(url) as entrada:
        print('Baixando arquivo...')
        dados = entrada.content.decode('latin1')
        print('Download completo')
        for cidade in csv.reader(dados.splitlines()):
            print('{}: {}'.format(cidade[8], cidade[3]))
        entrada.close()

    if entrada.ok:
        print('\nArquivo já foi fechado!')


if __name__ == '__main__':
    execute(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
