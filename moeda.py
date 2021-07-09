def aumentar(preco=0, taxa=0, f=False):
    res = preco + (preco * (taxa / 100))
    if f:
        return moeda(res)
    else:
        return res


def diminuir(preco=0, taxa=0, f=False):
    res = preco - (preco * (taxa / 100))
    if f:
        return moeda(res)
    else:
        return res


def dobro(preco=0, f=False):
    res = preco * 2
    if f:
        return moeda(res)
    else:
        return res


def metade(preco=0, f=False):
    res = preco / 2
    if f:
        return moeda(res)
    else:
        return res


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(n, a, d):
    print('=' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, d, True)}')
    print('=' * 30)
