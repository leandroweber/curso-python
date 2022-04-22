opcoes = [[1, 'Listar'],
          [2, 'Cadastrar'],
          [3, 'Excluir'],
          [4, 'Sair']]

def leiaInt(msg):
    while True:
        try:
           num = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return num


def leiaStr(msg):
    while True:
        try:
            texto = str(input(msg)).split()
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um texto válido.\033[m')
        else:
            if len(texto) == 0:
                print('\033[31mERRO! Digite um texto válido.\033[m')
            else:
                return texto


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu():
    cabecalho('MENU PRINCIPAL')
    for item in opcoes:
        print(f'\033[33m{item[0]}\033[m - \033[34m{item[1]}\033[m')
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc


