def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print('\033[31mERRO! Digite um valor válido.\033[m')
        else:
            valor = float(valor)
            break
    return valor


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            return 0
        else:
            return num



def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um numero real válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mNada digitado.\033[m')
            return 0
        else:
            return valor



def leiaStr(msg):
    while True:
        try:
            texto = str(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um texto válido.\033[m')
        else:
            return texto
