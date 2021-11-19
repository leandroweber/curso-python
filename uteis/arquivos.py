import os

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho/= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho/= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 1)
    return f'{tamanho}{texto}'


def percorreDir(pasta, termo, ext):
    cont = 0
    for raiz, diretorios, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if termo in arquivo:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                tamanho = os.path.getsize(caminho_completo)
                # print(nome_arquivo, ext_arquivo)
                if ext in ext_arquivo:
                    cont += 1                    
                    print(f'{caminho_completo} {formata_tamanho(tamanho)}')
                    # print('Arquivo:', arquivo)
                    # print('Caminho:', caminho_completo)
                    # print('Extensão:', ext_arquivo)
                    # print('Tamanho:', tamanho)
                    # print('Tamanho Fomatado:', formata_tamanho(tamanho))

    print('\nQuantidade:', cont)

if __name__ == '__main__':
    # caminho_procura = '/Users/Leandro/Documents/Projetos/Cursos/python/google'
    # termo_procura = ''
    # extensao_procura = 'qif'
    caminho_procura = input('Caminho a procurar: ')
    termo_procura = input('Termo que procura: ')
    extensao_procura = input('Extensão do arquivo: ')
    print()
    percorreDir(caminho_procura, termo_procura, extensao_procura)
