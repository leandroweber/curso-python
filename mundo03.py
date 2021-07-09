desafio = int(input('Escolha o desafio de 72 a 115: '))

# aula 16 tuplas
# tuplas são imutaveis
# del(tupla) # apaga da memoria

# variavel = 'abcdefghi'
# tupla = ('0=abc', '1=def', '2=ghi')
# lista = ['0=abc', '1=def', '2=ghi']
# dicionario = {'0=abc', '1=def', '2=ghi'}
# print(tupla[-1]) # o ultimo
# print(tupla[-2:]) # do penultimo ao final
# print(tupla[0:2]) # do primeiro ao segundo
# print(sorted(tupla)) # ordena
# print(len(tupla)) # itens
# print(tupla.count('1=def') # conta especifico
# print(tupla.index('1=def')) # posicao especico

# for d in tupla:
#     print(d)
# for c in range(0, len(tupla)):
#     print(c, tupla[c])
# for c, d in enumerate(tupla):
#     print(c, d)

if desafio == 72:
    print(f'Desafio {desafio}')
    extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
               'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
               'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
               'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
    while True:
        num = int(input('Digite um numero de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente', end='')
    print(f'O número digitado: {num} por extenso é {extenso[num]}')

elif desafio == 73:
    print(f'Desafio {desafio}')
    times = ('Flamengo', 'Internacional', 'Atlético MG', 'São Paulo', 'Fluminense',
             'Grêmio', 'Palmeiras', 'Santos', 'Athletico', 'Bragantino',
             'Ceará', 'Corinthias', 'Atlético GO', 'Bahia', 'Sport',
             'Fortaleza', 'Vasco', 'Goias', 'Coritiba', 'Botafogo')
    print('-=-' * 15)
    print(f'Lista de times {times}')
    print('-=-' * 15)
    print(f'Os 5 primeiros colocados são: {times[0:5]}')
    print('-=-' * 15)
    print(f'Os 4 útlimos colocados são: {times[-4:]}')
    print('-=-' * 15)
    print(f'Times em ordem alfbetica: {sorted(times)}')
    print('-=-' * 15)
    print(f'A Grêmio está na {times.index("Grêmio")+1}º colocação')
    print('-=-' * 15)

elif desafio == 74:
    print(f'Desafio {desafio}')
    from random import randint
    sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print('A lista dos números da sorteados são:', end='')
    for d in sorteados:
        print(f' {d}', end='')
    print(f'\nO menor número é: {min(sorteados)}')
    print(f'O maior número é: {max(sorteados)}')

elif desafio == 75:
    print(f'Desafio {desafio}')
    numeros = (int(input('Digite 1 valor: ')),
               int(input('Digite 2 valor: ')),
               int(input('Digite 3 valor: ')),
               int(input('Digite 4 valor: ')))
    print(f'Você Digitou os números {numeros}')
    print(f'O número 9 apareceu {numeros.count(9)} vezes')
    if 3 in numeros:
        print(f'O número 3 digitado na {numeros.index(3) + 1}ª posição')
    else:
        print('O número 3 não foi digitado')
    print('Os números pares digitados foram:', end='')
    cont = 0
    for d in numeros:
        if d % 2 == 0:
            print(f' {d}', end='')
            cont += 1
    if cont == 0:
        print('Não foram digitados números pares')

elif desafio == 76:
    print(f'Desafio {desafio}')
    listagem = ('Lápis', 1.75,
                'Borracha', 2,
                'Caderno', 15.9,
                'Estojo', 25,
                'Transferidor', 4.2,
                'Compasso', 9.99,
                'Mochila', 120.32,
                'Canetas', 22.3,
                'Livro', 34.9)
    print('-' * 40)
    print(f'{"LISTAGEM DE PREÇOS":^40}',)
    print('-' * 40)
    for c in range(0, len(listagem)):
        if c % 2 == 0:
            print(f'{listagem[c]:.<29}', end='')
        else:
            print(f' R$ {listagem[c]:>7.2f}')
    print('-' * 40)

elif desafio == 77:
    print(f'Desafio {desafio}')
    listagem = ('aprender', 'programar', 'linguagem',
                'python', 'curso', 'gratis', 'estudar',
                'praticar', 'trabalhar', 'mercado',
                'programador', 'futuro')
    for palavra in listagem:
        print(f'\nNa palavra {palavra.upper()} temos', end='')
        for letra in palavra:
            if letra in 'aeiou':
                print(f' {letra}', end='')

# aula 17 listas parte 1
# lista = ['a', 'b', 'c', 'd']
# print(f'lista = {lista}')
# lista.append('f') # adiciona item no final da lista
# print(f'lista = {lista}')
# lista.insert(2,'h') # adiciona item na posição especifica da lista
# print(f'lista = {lista}')
# del lista[3] # remove posição especifica da lista
# print(f'lista = {lista}')
# lista.pop(3) # remove posição especifica da lista
# print(f'lista = {lista}')
# lista.pop() # remove o ultimo item da lista
# print(f'lista = {lista}')
# lista.remove('h') # remove o primeiro item conforme solicitado
# print(f'lista = {lista}')
# valores = list(range(1,11)) # cria itens conforme passagem de parametros
# print(f'valores = {valores}')
# valores.sort(reverse=True)  # ordena lista ao contrario
# print(f'valores ao contrario = {valores}')
# print(f'tamanho de valores = {len(valores)}') # tamanho da lista
# valores.sort() # ordena lista
# for v in valores:
#     print(f'{v}..', end='')
# print('\n')
# val = list()
# for c in range(0, 5):
#     val.append(int(input('Digite um valor: '))) # atribuir varios valores
# for c, v in enumerate(val): # enumera e pega valores
#     print(f'podição {c} valor: {v}',)
# a = [1, 2, 3, 4]
# b = a # liga as listas mas não copia
# c = a[:] # copia a lista para outra
# sum(a)  # soma dados da lista
# b[2] = 8
# print(f'a = {a}')
# print(f'b = {b}')
# print(f'c = {c}')
#
elif desafio == 78:
    print(f'Desafio {desafio}')
    val = list()
    for c in range(0, 5):
        val.append(int(input(f'Digite o {c+1}° valor: ')))
        '''if c == 0:
            maior = menor = val[0]
        else:
            if val[c] > maior:
                maior = val[c]
            if val[c] < menor:
                menor = val[c]'''
    maior = max(val)
    menor = min(val)
    print('-=-' * 20)
    print(f'Você digitou os valores {val}')
    print(f'O maior valor é {maior} e está nas posições: ', end='')
    for p, v in enumerate(val):
        if v == maior:
            print(f'{p+1}.. ', end='')
    print(f'\nO menor valor é {menor} e está nas posições: ', end='')
    for p, v in enumerate(val):
        if v == menor:
            print(f'{p+1}.. ', end='')

elif desafio == 79:
    print(f'Desafio {desafio}')
    valores = list()
    while True:
        val = int(input('Adicione um número a lista: '))
        if val in valores:
            print('Valor duplicado! Não adicionado')
        else:
            valores.append(val)
            print('Valor adicionado com sucesso...')
        while True:
            resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('ERRO! Digite apenas S ou N')
        if resp == 'N':
            break
    print('-=-' * 20)
    valores.sort()
    print(f'Os valores distintos digitados foram: {valores}')

elif desafio == 80:
    print(f'Desafio {desafio}')
    valores = list()
    for c in range(0, 5):
        val = int(input('Adicione um número a lista: '))
        if c == 0 or val > valores[-1]:
            valores.append(val)
            print('Adicionado ao final da lista...')
        else:
            pos = 0
            while pos <= len(valores):
                if val <= valores[pos]:
                    valores.insert(pos, val)
                    print(f'Adicionado na posição {pos} da lista...')
                    break
                pos += 1
    print('-=-' * 20)
    print(f'A lista de valores em ordem é: {valores}')

elif desafio == 81:
    print(f'Desafio {desafio}')
    valores = list()
    while True:
        val = int(input('Digite um numero: '))
        valores.append(val)
        while True:
            resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('ERRO! Digite apenas S ou N')
        if resp == 'N':
            break
    print('-=-' * 20)
    valores.sort(reverse=True)
    print(f'Sua lista contem {len(valores)} números')
    print(f'Sua lista ao contrario é {valores}')
    if 5 in valores:
        print('Sua lista contém o número 5')
    else:
        print('Sua lista NÃO contém o número 5')

elif desafio == 82:
    print(f'Desafio {desafio}')
    valores = list()
    p = list()
    i = list()
    while True:
        val = int(input('Digite um numero: '))
        valores.append(val)
        while True:
            resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('ERRO! Digite apenas S ou N')
        if resp == 'N':
            break
    for n in valores:
        if n % 2 == 0:
            p.append(n)
        else:
            i.append(n)
    print('-=-' * 20)
    print(f'Sua lista completa é {valores}')
    print(f'A lista de pares é {p}')
    print(f'A lista de impares é {i}')

elif desafio == 83:
    print(f'Desafio {desafio}')
    expressao = str(input('Digite uma expressão '))
    parenteses = list()
    for c in expressao:
        if c == '(':
            parenteses.append('(')
        elif c == ')':
            if len(parenteses) > 0:
                parenteses.pop()
            else:
                parenteses.append(')')
                break
    if len(parenteses) == 0:
        print('Sua espressão está correta')
    else:
        print('Sua expressão NÃO está correta')

# aula 18 listas parte 2
# lista compostas
# lista = [['abc', 1], ['def', 2], ['ghi', 3]]
# lista[1][0] = 'def'

elif desafio == 84:
    print(f'Desafio {desafio}')
    pessoas = []
    dado = []
    maiorpeso = menorpeso = 0
    print('Cadastro de pessoas:')
    print('-=' * 30)
    while True:
        dado.append(str(input('Nome: ')))
        dado.append(float(input('Peso: ')))
        if len(pessoas) == 0:
            maiorpeso = dado[1]
            menorpeso = dado[1]
        else:
            if dado[1] > maiorpeso:
                maiorpeso = dado[1]
            elif dado[1] < menorpeso:
                menorpeso = dado[1]
        pessoas.append(dado[:])
        dado.clear()
        while True:
            resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('ERRO! Digite apenas S ou N')
        if resp == 'N':
            break
    print('-=' * 30)
    print(f'Você cadastrou {len(pessoas)} pessoas.')
    print(f'O maior peso digitado foi {maiorpeso}kg. Peso de', end='')
    for p in pessoas:
        if p[1] == maiorpeso:
            print(f' [{p[0]}]',end='')
    print()
    print(f'O menor peso digitado foi {menorpeso}kg. Peso de', end='')
    for p in pessoas:
        if p[1] == menorpeso:
            print(f' [{p[0]}]',end='')
    print()

elif desafio == 85:
    print(f'Desafio {desafio}')
    numeros = [[], []]
    for cont in range(1, 8):
        num = int(input(f'Digite o {cont} numero: '))
        if num % 2 == 0:
            numeros[0].append(num)
        else:
            numeros[1].append(num)
    numeros[0].sort()
    numeros[1].sort()
    print('-=' * 30)
    print(f'Os valores pares são: {numeros[0]}')
    print(f'Os valores impares são: {numeros[1]}')

elif desafio == 86:
    print(f'Desafio {desafio}')
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    print('-=' * 30)
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[ {matriz[l][c]:>5} ]', end='')
        print()

elif desafio == 87:
    print(f'Desafio {desafio}')
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    somapares = somacoluna3 = maiorlinha2 = 0
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    print('-=' * 30)
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[ {matriz[l][c]:>5} ]', end='')
            if matriz[l][c] % 2 == 0:
                somapares += matriz[l][c]
            if c == 2:
                somacoluna3 += matriz[l][c]
            if l == 1 and matriz[l][c] > maiorlinha2:
                maiorlinha2 = matriz[l][c]
        print()
    print('-=' * 30)
    print(f'A soma dos valores pares é {somapares}')
    print(f'A soma dos valores da terceira coluna é {somacoluna3}')
    print(f'O maior valor da segunda linha é {maiorlinha2}')

elif desafio == 88:
    print(f'Desafio {desafio}')
    from random import randint
    from time import sleep
    jogos = []
    numeros = []
    print('_' * 40)
    print(f'{"JOGOS DA MEGASENA":^40}')
    print('_' * 40)
    num = int(input('Quantos jogos quer que eu sorteie? '))
    print('-=' * 3, f'SORTEANDO {num} JOGOS', '-=' * 3)
    for contjogo in range(0, num):
        contnum = 0
        while contnum <= 6:
            sorteado = randint(1, 60)
            if sorteado not in numeros:
                numeros.append(sorteado)
                contnum += 1
        numeros.sort()
        jogos.append(numeros[:])
        numeros.clear()
    for contjogo, jogo in enumerate(jogos):
        sleep(1)
        print(f'Jogo {contjogo+1}: {jogo}')
    print('-=' * 5, '< BOA SORTE >', '-=' * 5)

elif desafio == 89:
    print(f'Desafio {desafio}')
    turma = []
    print('-=' * 20)
    print(f'{"Cadasto de alunos e notas":^40}')
    print('-=' * 20)
    while True:
        nome = str(input('Nome aluno: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2
        turma.append([nome, [nota1, nota2], media])
        while True:
            resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('ERRO! Digite apenas S ou N')
        if resp == 'N':
            break
    print('-=' * 40)
    print(f'{"No.":<4}{"NOME":<20}{"MÉDIA":>5}')
    print('-' * 29)
    for n, aluno in enumerate(turma):
        print(f'{n:<3}', end=' ')
        print(f'{aluno[0]:19}', end=' ')
        print(f'{aluno[2]:>5.2f}')
    print('-' * 29)
    while True:
        n = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
        if n == 999:
            print('Finalizando programa!')
            break
        elif n >= len(turma):
            print('Número invalido!')
        else:
            print(f'As notas de {turma[n][0]} foram {turma[n][1][0]:.2f} e {turma[n][1][1]:.2f}')

# aula 19 dicionario
# dados = dict()
# dados = {}
# dados = {'nome':'Pedro', 'idade':25}
# print(dados['nome'])
# print(dados['idade'])
# dados['sexo'] = 'M' # adiciona campo
# del dados['idade'] # apaga campo
# filme = {'titulo':'Star War',
#          'ano':1977,
#          'diretor':'George Lucas'}
# print(filme.values()) # dados
# print(filme.keys()) # nome campos
# print(filme.items()) # dados e nome de campos
# for k, v in filme.items():
#     print(f'O {k} é {v}')
# locadora = [filme]
# locadora.append(filme.copy()) # para copiar dados semelhante ao filmes[:] das listas
# print(locadora[0]['ano'])

elif desafio == 90:
    print(f'Desafio {desafio}')
    dado = {}
    dado['nome'] =str(input('Nome: '))
    dado['media'] = float(input(f'Média de {dado["nome"]}: '))
    if dado["media"] >= 7:
        dado['situacao'] = 'Aprovado'
    elif dado["media"] >= 5:
        dado['situacao'] = 'Recuperação'
    else:
        dado['situacao'] = 'Reprovado'
    print('-=' * 20)
    for k, v in dado.items():
        print(f'  {k} é igual a {v}')

elif desafio == 91:
    print(f'Desafio {desafio}')
    from random import randint
    from time import sleep
    from operator import itemgetter
    ranking = []
    print('Valores sorteados:')
    jogo = {'jogador1': randint(1, 6),
            'jogador2': randint(1, 6),
            'jogador3': randint(1, 6),
            'jogador4': randint(1, 6)}
    for k, v in jogo.items():
        print(f'O {k} tirou {v}')
        sleep(1)
    print('-=' * 30)
    print('  == RANKING DOS JOGADORES ==')
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
    for i, v in enumerate(ranking):
        print(f'    {i+1} lugar, {v[0]} com {v[1]}')
        sleep(1)

elif desafio == 92:
    print(f'Desafio {desafio}')
    from datetime import date
    anotual = date.today().year
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    nascimento = int(input('Ano de Nascimento: '))
    pessoa['idade'] = anotual - nascimento
    pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if pessoa['ctps'] != 0:
        pessoa['contratacao'] = int(input('Ano de contratação: '))
        pessoa['salario'] = float(input('Salário: R$ '))
        pessoa['apodentadoria'] = pessoa['contratacao'] + 35 - anotual + pessoa['idade']
    print('-=' * 30)
    print(f'{pessoa}')
    for k, v in pessoa.items():
        print(f'    -{k} tem o valor {v}')

elif desafio == 93:
    print(f'Desafio {desafio}')
    jogador = {}
    gol = []
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, partidas):
        gol.append(int(input(f'   Quantos gols na partida {p+1}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    print('-=' * 30)
    print(f'{jogador}')
    print('-=' * 30)
    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}.')
    print('-=' * 30)
    print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
    for p, g in enumerate(jogador['gols']):
        print(f'    => Na partida {p+1}, fez {g} gols.')
    print(f'Fez um total de {jogador["total"]} gols.')

elif desafio == 94:
    print(f'Desafio {desafio}')
    dado = {}
    pessoas = []
    somaidade = media = 0
    while True:
        dado['nome'] = str(input('Nome: '))
        dado['sexo'] = ' '
        while dado['sexo'] not in 'MF':
            dado['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
            if dado['sexo'] not in 'MF':
                print('ERRO! Por favor, digite apenas M ou F')
        dado['idade'] = int(input('Idade: '))
        somaidade += dado['idade']
        pessoas.append(dado.copy())
        dado.clear()
        while True:
            resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('ERRO! Digite apenas S ou N')
        if resp == 'N':
            break
    print('-='* 30)
    print(f'{pessoas}')
    print('-=' * 30)
    print(f'A)- Ao todo temos {len(pessoas)} pessoas.')
    media = somaidade / len(pessoas)
    print(f'B)- A média de idade é de: {media:.2f} anos.')
    print('C)- As mulheres cadastradas foram:', end=' ')
    for d in pessoas:
        if d['sexo'] == 'F':
            print(f'{d["nome"]}', end=' ')
    print('')
    print('D)- Lista das pessoas que estão cima da média:')
    for d in pessoas:
        if d['idade'] >= media:
            print('    ', end='')
            for k, v in d.items():
                print(f'{k} = {v}; ', end='')
            print()
    print('Encerrado')

elif desafio == 95:
    print(f'Desafio {desafio}')
    jogador = {}
    lista = []
    gol = []
    while True:
        jogador['nome'] = str(input('Nome do jogador: '))
        partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        gol.clear()
        for p in range(0, partidas):
            gol.append(int(input(f'Quantos gols na partida {p + 1}? ')))
        jogador['gols'] = gol[:]
        jogador['total'] = sum(gol)
        lista.append(jogador.copy())
        while True:
            resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
            if resp in 'SN':
                break
            print('ERRO! Digite apenas S ou N')
        if resp == 'N':
            break
    print('-=' * 30)
    print('cod ', end='')
    for k in jogador.keys():
        print(f'{k:<15}', end='')
    print()
    print('-' * 60)
    for k, v in enumerate(lista):
        print(f'{k:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    print('-' * 60)
    while True:
        opcao = int(input('Mostrar dados de qual jogador? (999 para sair) '))
        if opcao == 999:
            break
        elif opcao >= len(lista):
            print(f'ERRO! Não existe jogador com código {opcao}! Tente novamente')
        else:
            print(f'--LEVANTAMENTO DO JOGADOR {lista[opcao]["nome"]}')
            for jog, gol in enumerate(lista[opcao]["gols"]):
                print(f'  No jogo {jog+1} fez {gol} gols')
        print('-' * 60)
    print('<< FINAL DO PROGRAMA>>')

# aula 20 funções parte 1
# def cabec(msg, tam):
#     print('-' * tam)
#     print(f'{msg:^{tam}}')
#     print('-' * tam)
#
# cabec('abc', 100)
#
# def contador(* num): # cria uma tupla
#     print(num)
#
# contador(2, 1, 3)
#
# def soma(* valores): # cria uma tupla
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} temos {s}')
#
# soma(5, 3, 4)
# soma(2, 4, 7, 3, 2, 1)
#
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
# valores = [2, 4, 6, 2, 5]
# dobra(valores) # atualizou a lista
# print(valores)

elif desafio == 96:
    print(f'Desafio {desafio}')

    def cabec(msg, tam):
        print('-' * tam)
        print(f'{msg:^{tam}}')
        print('-' * tam)

    def area(l, c):
        a = l * c
        print(f'A area de um terrono de {l} x {c} é de {a}m2')


    # Programa Principal
    cabec('Controle de Terrenos', 30)
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    area(larg, comp)

elif desafio == 97:
    print(f'Desafio {desafio}')

    def cabec(msg):
        tam = len(msg) + 4
        print('~' * tam)
        print(f'{msg:^{tam}}')
        print('~' * tam)


    # Programa Principal
    cabec('Olá Mundo!')
    cabec('Leandro Weber')
    cabec('Curso de Pyton no Youtube')

elif desafio == 98:
    print(f'Desafio {desafio}')
    from time import sleep

    def cabec(tam):
        print('-=' * tam)

    def contador(ini, fim, pas):
        if pas == 0:
            pas = 1
        print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
        if fim < ini:
            fim -= 1
            if pas > 0:
                pas *= -1
        else:
            fim += 1
            if pas < 0:
                pas *= -1
        for i in range(ini, fim, pas):
            print(f'{i} ', end='')
            sleep(0.2)
        print('FIM!')


    # Programa Principal
    cabec(20)
    contador(1, 10, 1)
    cabec(20)
    contador(10, 0, 2)
    cabec(20)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    final = int(input('Final:  '))
    passo = int(input('Passo:  '))
    contador(inicio, final, passo)

elif desafio == 99:
    print(f'Desafio {desafio}')
    from random import randint
    from time import sleep

    def maior(* valores):
        print('-=' * 20)
        print('Analisando os valores passados...')
        max = 0
        for num in valores:
            sleep(0.5)
            print(num, end=' ')
            if num > max:
                max = num
        print(f'Foram infomados {len(valores)} valores ao todo.')
        print(f'O maior valor informado foi {max}')

    #Programa principal
    maior(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
    maior(randint(0, 9), randint(0, 9), randint(0, 9))
    maior(randint(0, 9), randint(0, 9))
    maior(randint(0, 9))
    maior()

elif desafio == 100:
    print(f'Desafio {desafio}')
    from random import randint
    from time import sleep

    def sorteio(lst):
        print('Sorteando 5 valores da lista: ', end='')
        for i in range(0, 5):
            sleep(0.3)
            num = randint(0, 9)
            print(num, end=' ')
            lst.append(num)
        print('PRONTO!')

    def chamaPar(lst):
        pares = 0
        for num in lst:
            if num % 2 == 0:
                pares += num
        print(f'Somando os valores pares de {lst}, temos {pares}')


    # Programa principal
    numeros = []
    sorteio(numeros)
    chamaPar(numeros)

# aula 21 funções parte 2

# interaction help
# help(print)
# help(if)

# def funcao(a, b, c):
# docstrings
#    """
#    a = para que serve a
#    b = para que serve b
#    c = para que serve c
#    retorno = funcao sem retorno
#    """
# help(funcao) retorna o docstring da funcao criadda
# argumentos opcionais
# b=0 c=0 deixa o valor nao obrigatorio
# def funcao1(b=0,c=0):
# escopo de variavel
#    global a  # trata uma variavel que já existe no programa principal
#    return a
# r1 = funcao1() # valor de a salva em r1

elif desafio == 101:
    print(f'Desafio {desafio}')
    def voto(ano):
        """
        => verifica conforme a idade se o voto é: Obrigatorio, Opcional ou Negado
        :param ano: ano de nascimento
        :return: str
        """
        from datetime import date
        atual = date.today().year
        idade = atual - ano
        if idade >= 18 and idade <= 65:
            opcao = 'OBRIGATORIO'
        elif idade >= 16:
            opcao = 'OPCIONAL'
        else:
            opcao = 'NÃO VOTA'
        return (f'Com {idade} anos: VOTO {opcao}')

    # Programa principal
    print('-' * 20)
    print(voto(int(input('Em que ano você nasceu? '))))

elif desafio == 102:
    print(f'Desafio {desafio}')

    def fatorial(n, show=False):
        """"
        => Calcula a fatorial de um numero
        :param n: numero a ser calculado
        :param show: [opcional] Mostrar ou não a conta
        :return: o valor da fatorial de um numero n
        """
        fatorial = 1
        print('Calculando {}! = '.format(n), end='')
        for c in range(n, 0, -1):
            if show:
                print(c, end='')
                if c > 1:
                    print(' x ', end='')
                else:
                    print(' = ', end='')
            fatorial *= c
        return fatorial


    # Programa principal
    num = int(input('Numero para fatorial: '))
    exibir = str(input('Exibir calculo [S/N]: ')).strip().upper()[0]
    if exibir == 'S':
        print(f'{fatorial(num, True)}')
    else:
        print(f'{fatorial(num)}')

elif desafio == 103:
    print(f'Desafio {desafio}')

    def ficha(n='<desconhecido>', g=0):
        """"
        => exibibe uma msg
        :param n: [opcional] nome do jogador
        :param g: [opcional] numero de gosl
        :return: sem retorno
        """
        print(f'O jogador {n} fez {g} gols no campeonato')

    print('-' * 20)
    nome = input('Nome do jogador: ')
    gol = input('Número de gols: ')
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    if nome.strip() == '':
        ficha(g=gol)
    else:
        ficha(nome, gol)

elif desafio == 104:
    print(f'Desafio {desafio}')

    def leiaInt(msg):
        while True:
            num = input(msg)
            if num.isnumeric():
                n = int(num)
                break
            else:
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        return n

    # Programa principal
    numero = leiaInt('Digite um número: ')
    print(f'Voce acabou de digitar o número {numero}')

elif desafio == 105:
    print(f'Desafio {desafio}')

    def notas(* valores, sit=False):
        """
        => Função para analizar notas de vários alunos.
        :param valores: uma ou mais notas dos alunos
        :param sit: [opcional], exibir a situação da turma
        :return: dicionario com varias informações sobre a turma
        """
        dic = {}
        dic['total'] = len(valores)
        dic['maior'] = max(valores)
        dic['menor'] = min(valores)
        dic['media'] = sum(valores) / len(valores)
        if sit:
            if dic['media'] >= 7:
                dic['situacao'] = 'BOA'
            elif dic['media'] >= 5:
                dic['situacao'] = 'RAZOAVEL'
            else:
                dic['situacao'] = 'RUIM'
        return dic

    # Programa principal
    resp = notas(5.5, 6, 8, 2, 5, sit=True)
    print(resp)
    # help(notas)

elif desafio == 106:
    print(f'Desafio {desafio}')
    from time import sleep

    cor = ['\033[m',    # 0 = vazio
           '\033[42m',  # 1 = verde
           '\033[46m',  # 2 = cianeto
           '\033[41m',  # 3 = vermelho
           '\033[7m']   # 4 = branco

    def cabec(msg, cod):
        tam = len(msg) + 4
        print(cor[cod], end='')
        print('~' * tam)
        print(f'  {msg}  ')
        print('~' * tam)
        sleep(1)

    def ajuda(com):
        cabec(f'Acessando o manual do comando \'{funcao}\'', 2)
        print(cor[4], end='')
        help(com)
        print(cor[0], end='')
        sleep(2)


    # Programa principal
    while True:
        cabec('SISTEMA DE AJUDA PYHELP', 1)
        funcao = input(f'{cor[0]}Função ou biblioteca> [Fim para sair]: ').lower().strip()
        if funcao == 'fim':
            break
        ajuda(funcao)
    cabec('Até logo', 3)

# aula 22 módulos e pacotes
# def = function
# modulos = criar arquivos separados com funções/def
# pacotes= criar pastas no projeto e no arquivo __init__.py adicionar as funções/def
# chamar esse arquivos separados com import = {include.i}
elif desafio == 107:
    print(f'Desafio {desafio}')
    import moeda
    p = float(input('Digite o preço R$ '))
    print(f'A metade de {p} é {moeda.metade(p)}')
    print(f'O dobro de {p} é {moeda.dobro(p)}')
    print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
    print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')

elif desafio == 108:
    print(f'Desafio {desafio}')
    import moeda
    p = float(input('Digite o preço R$ '))
    print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
    print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
    print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
    print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')

elif desafio == 109:
    print(f'Desafio {desafio}')
    import moeda
    p = float(input('Digite o preço R$ '))
    print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
    print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
    print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
    print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')

elif desafio == 110:
    print(f'Desafio {desafio}')
    import moeda
    p = float(input('Digite o preço R$ '))
    moeda.resumo(p, 80, 35)

elif desafio == 111:
    print(f'Desafio {desafio}')
    from cursoCeV import moeda
    p = float(input('Digite o preço R$ '))
    moeda.resumo(p, 80, 35)

elif desafio == 112:
    print(f'Desafio {desafio}')
    from cursoCeV import moeda, dado
    p = dado.leiaDinheiro('Digite o preço R$')
    moeda.resumo(p, 80, 35)

# aula 23 tratamentos de erros e exeções
# try:
#     n1 = int(input('Digite um numero inteiro: '))
#     div = int(input('Divisor: '))
#     val = n1 / div
# except (TypeError, ValueError):
#     print('\033[31mValor precisa ser inteiro\033[m')
# except ZeroDivisionError:
#     print(f'\033[31mDivisor não pode ser 0\033[m')
# except KeyboardInterrupt:
#     print('O Usuario não informou os dados')
# except OSError:
#     print('\033[31merro oserror\033[m')
# except Exception as erro:
#     # acessa o erro
#     print(f'Problema encontrado {erro.__class__}')
#     print(f'Problema encontrado {erro.__cause__}')
# except:
#    print(f'\033[31mInfelizmente tivemos um problema\033[m')
# else:
#     # deu certo
#     print(f'valor dividido {val:.2f}')
# finally:
#     # certo ou falha
#     print('Fim do programa')

elif desafio == 113:
    print(f'Desafio {desafio}')
    from cursoCeV import dado
    inte = dado.leiaInt('Digite um inteiro: ')
    real = dado.leiaFloat('Digite um real: ')
    print(f'O valor inteiro foi {inte} e o real foi {real}')

elif desafio == 114:
    print(f'Desafio {desafio}')
    import urllib.request
    try:
        site = urllib.request.urlopen("http://pudim.com.br/")
    except:
        print('\033[31mO site Pudim não está acessível no momento.\033[m')
    else:
        print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
        #print(site.read())

elif desafio == 115:
    print(f'Desafio {desafio}')
    from ex115.inicio import Start
    import ex115.inicio
    s = Start
    s.comeca()

elif desafio == 116:
    print(f'Desafio {desafio}')
    from cursoCeV import dado
    from time import sleep
    tam = 60
    cadastro = []
    pessoa = {'nome': '', 'idade': 0}

    def cabec(msg):
        print('-' * tam)
        #print(f'{msg:^{tam}}')
        print(msg.center(tam))
        print('-' * tam)
        sleep(0.3)


    def menu(lista):
        c = 1
        for item in lista:
            print(f'{c} - {item}')
            c += 1
        print('-' * tam)


    def listar():
        cabec('PESSOAS CADASTRADAS')
        print('Cod', f'{"Nome":<30}', f'{"Idade"}')
        for k, v in enumerate(cadastro):
            print(f'{k:<3} ', end='')
            print(f'{v["nome"]:<30} {v["idade"]} ')


    def cadastrar():
        cabec('CADASTRAR PESSOA')
        pessoa["nome"] = dado.leiaStr('Nome: ')
        pessoa["idade"] = dado.leiaInt('Idade: ')
        cadastro.append(pessoa.copy())
        print(f'Novo registro {pessoa["nome"]} adicionado')


    def excluir():
        cabec('EXCLUIR PESSOA')
        cod = dado.leiaInt('Código da Pessoa: ')
        opcao = str(input(f'Tem certeza de excluir o cadastro "{cadastro[cod]["nome"]}" ? [S/N]: ')).strip().upper()[0]
        if opcao == 'S':
            del cadastro[cod]
            print(f'Cadastro "{cadastro[cod]["nome"]}" EXCLUÍDA')
        else:
            print(f'Cadastro "{cadastro[cod]["nome"]}" NÃO excluída')


    while True:
        cabec("MENU PRINCIPAL")
        menu(['Listar', 'Cadastrar', 'Excluir', 'Sair'])
        opcao = dado.leiaInt('Sua opção: ')
        if opcao == 1:
            listar()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            break
        else:
            print('ERRO! Digite uma opção válida!')
    cabec('Sair do Sistema... Até logo')

else:
    print('Opção inválida')
