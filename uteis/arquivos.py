import os, shutil

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


def percorreDir(pasta, termo='', ext=''):
    # termo = '2021-1'
    # ext = 'qif'
    cont = 0
    for raiz, diretorios, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if termo in arquivo:
                caminho_completo = os.path.join(raiz, arquivo)
                tamanho = os.path.getsize(caminho_completo)
                # nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                # print(nome_arquivo, ext_arquivo)
                if ext in arquivo:
                    cont += 1                    
                    print(f'{caminho_completo} {formata_tamanho(tamanho)}')
                    # print('Arquivo:', arquivo)
                    # print('Caminho:', caminho_completo)
                    # print('Extensão:', ext_arquivo)
                    # print('Tamanho:', tamanho)
                    # print('Tamanho Fomatado:', formata_tamanho(tamanho))

    print('\nQuantidade:', cont)


def criaDir(caminho):
    try:
        os.mkdir(caminho)
    except FileExistsError as e:
        print(f'Pasta {caminho} -> já existe')
    else:
        print(f'Pasta {caminho} -> criada')


def copiarMoverArq(caminho_original, caminho_novo, mover=False, excluir=False, termo=''):
    termo = '123'
    for root, dirs, files in os.walk(caminho_original):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_novo, file)
    
            if termo in file:
                if mover:
                    shutil.move(old_file_path, new_file_path)
                    print(f'Arquivo: {file} movido')
                else:
                    shutil.copy(old_file_path, new_file_path)
                    print(f'Arquivo: {file} copiado')

                if excluir:
                    os.remove(new_file_path)
                    print(f'Arquivo: {file} excluído')



if __name__ == '__main__':
    # caminho_procura = '/Users/Leandro/Documents/Projetos/Cursos/python/google'
    # caminho_procura = r'c:\Users\Leandro\Documents\Projetos\Cursos\python\google'
    caminho_procura = input('Caminho a procurar: ')
    termo_procura = input('Termo que procura: ')
    extensao_procura = input('Extensão do arquivo: ')
    print()
    percorreDir(caminho_procura, termo_procura, extensao_procura)
    
    # caminho_novo = r'C:\Users\Leandro\Documents\Saúde\teste'
    # caminho_origem = r'C:\Users\Leandro\Documents\Saúde\teste1'
    # criaDir(caminho_novo)
    # copiarMoverArq(caminho_origem, caminho_novo, mover=False, excluir=False)

