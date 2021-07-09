from lib.interface import *
from lib.arquivo import *
from time import sleep


class Start:
    def __init__(self):
        print('start')

    @staticmethod
    def comeca():
        while True:
            opcao = menu()
            if opcao == 1:
                cabecalho(f'{opcao} - LISTAR PESSOAS')
                lerArquivo()
            elif opcao == 2:
                cabecalho(f'{opcao} - CADASTRAR PESSOA')
                nome = leiaStr('Nome: ')
                idade = leiaInt('Idade: ')
                cadastrar(nome, idade)
            elif opcao == 3:
                cabecalho(f'{opcao} - EXCLUIR PESSOA')
                cod = leiaInt('Código: ')
                lerArquivo(cod)
            elif opcao == 4:
                cabecalho('Saindo do Sistema!')
                break
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
            sleep(1)
