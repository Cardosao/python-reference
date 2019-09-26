#!/usr/bin/env python3

class console_dumper:
    NORMAL = '\033[0m'
    ERRO = '\033[1;31m'
    HELP = '\033[1;96m'

    def console_error_dumper(mensagem):
        print(ERRO + mensagem + NORMAL)


    def console_help_dumper(mensagem):
        print(HELP + mensagem + NORMAL)

