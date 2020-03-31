#!/usr/bin/env python
#ARQUIVO PARA EXECUTAR COMANDOS DE GERENCIAMENTO DO DJANGO FRAMEWORK
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    #Variaveis de ambiente
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto1.settings')
    try:
        #Biblioteca para executar comando no CMD
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    #ARGUMENTO DOS COMANDOS ENTRAM NO SYS.ARGV
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
