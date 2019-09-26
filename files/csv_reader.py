#!/usr/bin/env python3


try:
    arquivo = open('../pessoas.csv')
    dados = arquivo.read()
    arquivo.close()
    for registro in dados.splitlines():
        print('Nome: {}, idade {}'.format(*registro.split(',')))
except IndexError:
    print(IndexError)
finally:
    print('finally')
    arquivo.close()
    print(arquivo.closed)


try:
    arquivo = open('../pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, idade {}'.format(*registro.strip().split(',')))
except IndexError:
    print(IndexError)
finally:
    print('finally')
    arquivo.close()
    print(arquivo.closed)

with open('../pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, idade {}'.format(*registro.strip().split(',')))


if arquivo.closed:
    print('arquivo fechado!')


texto1 = '   texto1   '.strip()
texto2 = '0000texto20000'.strip('0')
print(texto1, texto2)
