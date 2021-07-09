# opcoes arquivo
# r = ler
# w = escrever
# a = adicionar
# t = texto
# + = criar arquivo
arq = 'dados.txt'
cadastro = []

def inicioArq():
    if not arquivoExiste():
        criarArquivo()


def arquivoExiste():
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo():
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print(f'\033[31mERRO! Arquivo {arq} NÃO criado!\033[m')
    else:
        print(f'\033[32mArquivo {arq} criado com sucesso!\033[m')


def lerArquivo(cod=0):
    inicioArq()
    cont = 0
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        #print(a.read())
        for linha in a:
            #print(linha)
            dado = linha.split(';')
            #print(dado)
            dado[1] = dado[1].replace('\n', '')
            cont += 1
            if cod == 0:
                print(f'{cont:<4}{dado[0]:<30}{dado[1]:>3} anos')
            else:
                cadastro.append(dado[:])
                excluir(cod)
    finally:
        a.close()


def cadastrar(nome='desconhecido', idade=0):
    try:
        inicioArq()
        a = open(arq, 'at')
    except:
        print('\033[31mErro ao ler arquivo\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mERRO! Na escrita dos dados!\033[m')
        else:
            print(f'\033[32mNome "{nome}" salvo com sucesso!\033[m')
            a.close()


def excluir(num):
    cont = 0
    try:
        a = open(arq, 'wt')
    except:
        print('\033[31mERRO! Na exclusão dos dados!\033[m')
    else:
        for linha in cadastro:
            cont += 1
            if cont == num:
                print(f'\033[32mCódigo "{num}" excluído com sucesso!\033[m')
            else:
                a.write(f'{linha[0]};{linha[1]}\n')
        a.close()


# Leandro;42
# Julia;7
# Fabiana;42
# Margarida;76
