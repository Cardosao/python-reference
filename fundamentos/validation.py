#!/usr/bin/env python3
import sys
import errno
from math import pi


class TerminalColor:
    NORMAL = '\033[0m'
    ERRO = '\033[1;31m'
    HELP = '\033[1;96m'


def help():
    console_help_dumper("É necessário informar o raio do circulo!")
    console_help_dumper('Sintaxe: {} <raio>'.format(sys.argv[0]))


def circulo(raio):
    return pi * float(raio) ** 2


def console_error_dumper(mensagem):
    print(TerminalColor.ERRO + mensagem + TerminalColor.NORMAL)


def console_help_dumper(mensagem):
    print(TerminalColor.HELP + mensagem + TerminalColor.NORMAL)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        console_error_dumper('O raio deve ser um valor numerico')
        sys.exit(errno.EINVAL)

    raio = int(sys.argv[1])
    if 0 < raio <= 100:
        area = circulo(raio)
        print('Area do circulo: ', area)
    else:
        print('Valor fora do range 1 a 100: ')
