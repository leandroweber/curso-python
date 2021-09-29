desafio = int(input('Escolha o desafio de 1 a 35? '))

inicio = '\033['
final = 'm'
estilo = {'vazio': '0',  # none
          'negrito': '1',  # bold
          'sublinhado': '4',  # underline
          'negativo': '7'}  # 7 = negative
cortexto = {'limpa': '',
            'branco': '30',
            'vermelho': '31',
            'verde': '32',
            'amarelo': '33',
            'azul': '34',
            'roxo': '35',
            'cianeto': '36',
            'cinza': '37'}
corfundo = {'limpa': '',
            'branco': '40',
            'vermelho': '41',
            'verde': '42',
            'amarelo': '43',
            'azul': '44',
            'roxo': '45',
            'cianeto': '46',
            'cinza': '47'}


# aula aula 05
def opcao1():
    print(f'Desafio {desafio}')
    msg = 'Olá Mundo!'
    print(inicio + estilo['sublinhado'] + ';' + cortexto['azul'] + final + msg)


def opcao2():
    print(f'Desafio {desafio}')
    nome = input('Qual é seu nome: ')
    print('É um prazer te conhecer, {}{}'.format(inicio + cortexto['vermelho'] + final, nome))


if desafio == 3:
    print('Desafio {}'.format(desafio))
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite mais número: '))
    s = n1 + n2
    print(type(n1))
    print(f'A soma entre {n1} e {n2} vale: {s}')
    """"
    print('A soma entre {}{}{} e {}{}{} vale: {}{}{}'.format(inicio + cortexto['azul'] + final,
                                                             n1,
                                                             inicio + final,
                                                             inicio + cortexto['verde'] + final,
                                                             n2,
                                                             inicio + final,
                                                             inicio + corfundo['cinza'] + final,
                                                             s,
                                                             inicio + final ))
    """
'''
# AULA 6
elif desafio == 4:
    print('Desafio {}'.format(desafio))
    valor = input('digite algo: ')
    print('o tipo primitivo é {}{}{}'.format(inicio + cortexto['roxo'] + final, type(valor), inicio + final))
    print('só tem espaço? {}{}{}'.format(inicio + cortexto['roxo'] + final, valor.isspace(), inicio + final))
    print('é um número? {}{}{}'.format(inicio + cortexto['roxo'] + final, valor.isnumeric(), inicio + final))
    print('é alfabético? {}{}{}'.format(inicio + cortexto['roxo'] + final, valor.isalpha(), inicio + final))
    print('é alfanumerico? {}{}{}'.format(inicio + cortexto['roxo'] + final, valor.isalnum(), inicio + final))
    print('está em maiuscula? {}{}{}'.format(inicio + cortexto['roxo'] + final, valor.isupper(), inicio + final))
    print('está em minuscula? {}{}{}'.format(inicio + cortexto['roxo'] + final, valor.islower(), inicio + final))
    print('está capitalizado? {}{}{}'.format(inicio + cortexto['roxo'] + final, valor.istitle(), inicio + final))

# AULA 7 - OPERADORES ARITMETICOS
# ordem de precedencia de calculo
# 1 ()
# 2 **
# 3 * ou / ou // ou %
# 4 + ou -

# 5 + 2 == 7 soma
# 5 - 2 == 3 subtração
# 5 * 2 == 10 multiplicação
# 5 / 2 == 2.5 divisão
# 5 ** 2 == 25 potencia
# 5 // 2 == 2 inteiro da divisao
# 5 % 2 == 1 resto da divisao

# 5+3*2 == 11
# 3*5+4**2 == 31
# 3*(5+4)**2 == 243

# print('exercicio 005')
# n1 = int(input('numero 1: '))
# n2 = int(input('numero 2: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma é {},\n o produto é {}, a divisao é {:.3f}'.format(s, m, d), end=' >>> ')
# print('Divisão inteira é {}, a potencia é {}'.format(di, e))

# valor = 'lele'
# print('valor {:<20}!'.format(valor))
# verificar {:=>20}

elif desafio == 5:
    print('Desafio {}'.format(desafio))
    n1 = int(input('Digite um numero : '))
    print('numero= {}{}{}\nsucessor= {}{}{}\nantecessor= {}{}'.format(inicio + cortexto['amarelo'] + final,
                                                                      n1,
                                                                      inicio + final,
                                                                      inicio + cortexto['vermelho'] + final,
                                                                      n1 + 1,
                                                                      inicio + final,
                                                                      inicio + cortexto['azul'] + final,
                                                                      n1 - 1))

elif desafio == 6:
    print('Desafio {}'.format(desafio))
    num = int(input('numero : '))
    print('numero= {}\ndobro= {}\ntriplo= {}\nraiz quadrado= {:.2f}'.format(num, num * 2, num * 3, num ** (1 / 2)))

elif desafio == 7:
    print('Desafio {}'.format(desafio))
    nota1 = float(input('nota 1 : '))
    nota2 = float(input('nota 2 : '))
    print('A média de {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, (nota1 + nota2) / 2))

elif desafio == 8:
    print('Desafio {}'.format(desafio))
    m = float(input('valor em metros : '))
    km = m / 1000
    hm = m / 100
    dam = m / 10
    dm = m * 10
    cm = m * 100
    mm = m * 1000
    print('A medida de {}m corresponde a \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m, km, hm, dam, dm, cm, mm))

elif desafio == 9:
    print('Desafio {}'.format(desafio))
    num = int(input('numero : '))
    print('-' * 12)
    print('{} x {:2} = {}'.format(num, 1, num * 1))
    print('{} x {:2} = {}'.format(num, 2, num * 2))
    print('{} x {:2} = {}'.format(num, 3, num * 3))
    print('{} x {:2} = {}'.format(num, 4, num * 4))
    print('{} x {:2} = {}'.format(num, 5, num * 5))
    print('{} x {:2} = {}'.format(num, 6, num * 6))
    print('{} x {:2} = {}'.format(num, 7, num * 7))
    print('{} x {:2} = {}'.format(num, 8, num * 8))
    print('{} x {:2} = {}'.format(num, 9, num * 9))
    print('{} x {:2} = {}'.format(num, 10, num * 10))
    print('-' * 12)

elif desafio == 10:
    print('Desafio {}'.format(desafio))
    n1 = float(input('em carteira R$:'))
    c = float(input('Cotação US$:'))
    print('com R$ {:.2f}, compra US$ {:.2f}, na cotacao US$ 1.00 = R$ {}'.format(n1, n1 / c, c))

elif desafio == 11:
    print('Desafio {}'.format(desafio))
    larg = float(input('Largura da parede: '))
    alt = float(input('Altura da parede: '))
    area = larg * alt
    tinta = area / 2
    print('Parede de dimensão {}x{} com area de {}m2.\nnecessarios {}l de tinta'.format(larg, alt, area, tinta))

elif desafio == 12:
    print('Desafio {}'.format(desafio))
    valor = float(input('Valor: R$'))
    desconto = float(input('Desconto: '))
    novo = valor - (valor * desconto / 100)
    print('Valor anterior {:.2f}, desconto= {}%, novo valor= {:.2f}'.format(valor, desconto, novo))

elif desafio == 13:
    print('Desafio {}'.format(desafio))
    salario = float(input('Salario R$'))
    reajuste = float(input('Reajuste: '))
    novo = salario + (salario * reajuste / 100)
    print('Salario R${:.2f}, reajuste= {}%, novo salario R${:.2f}'.format(salario, reajuste, novo))

elif desafio == 14:
    print('Desafio {}'.format(desafio))
    c = float(input('Temperatura em C'))
    f = ((9 * c) / 5) + 32
    print('Temperatura de {} C corresponde a {}F'.format(c, f))

elif desafio == 15:
    print('Desafio {}'.format(desafio))
    dias = int(input('Quantos dias alugado? '))
    km = float(input('Quantos Km rodados? '))
    valor = (60 * dias) + (km * 0.15)
    print('O valor a ser pago é de R${:.2f}'.format(valor))

# aula 08
# import emoji
# print(emoji.emojize('Olá mundo :earth_americas:', use_aliases=True))

elif desafio == 16:
    print('Desafio {}'.format(desafio))
    num = float(input('Digite um numero: '))
    # from math import trunc
    # print('A numero {} tem porção inteira {}'.format(num, trunc(num)))
    print('A numero {} tem porção inteira {}'.format(num, int(num)))

elif desafio == 17:
    print('Desafio {}'.format(desafio))
    co = float(input('Comprimento do cateto oporto: '))
    ca = float(input('Comprimento do cateto adjacento: '))
    # hi = (co ** 2 + ca ** 2) ** 1/2
    from math import hypot
    hi = hypot(co, ca)
    print('A hipotenusa vai medir {:.2f }'.format(hi))

elif desafio == 18:
    print('Desafio {}'.format(desafio))
    from math import radians, sin, cos, tan
    angulo = float(input('Digite o ângulo que você deseja: '))
    seno = sin(radians(angulo))
    print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
    cosseno = cos(radians(angulo))
    print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
    tangente = tan(radians(angulo))
    print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

elif desafio == 19:
    print('Desafio {}'.format(desafio))
    from random import choice  # Sorteio de valor
    n1 = str(input('Primeiro aluno: '))
    n2 = str(input('Segundo aluno: '))
    n3 = str(input('Terceiro aluno: '))
    n4 = str(input('Quarto aluno: '))
    lista = [n1, n2, n3, n4]
    escolhido = choice(lista)
    print('O aluno esccolhido foi {}'.format(escolhido))

elif desafio == 20:
    print('Desafio {}'.format(desafio))
    from random import shuffle  # Reordenar lista
    n1 = str(input('Primeiro aluno: '))
    n2 = str(input('Segundo aluno: '))
    n3 = str(input('Terceiro aluno: '))
    n4 = str(input('Quarto aluno: '))
    lista = [n1, n2, n3, n4]
    shuffle(lista)
    print('A ordem de apresentação será\n {}'.format(lista))

elif desafio == 21:
    print('Desafio {}'.format(desafio))
    print('tocar musica mp3')
    from pygame import mixer
    mixer.init()
    mixer.music.load('09-bruno_mars-count_on_me.mp3')
    mixer.music.play()
    print('não tocou')

# aula 09
# frase = 'Curso em Video Python'
# print(frase)
# print('012345678901234567890')
# print('frase[9:13] {}'.format(frase[9:13]))
# print('frase[9:] {}'.format(frase[9:]))
# print('frase[0:5] {}'.format(frase[0:5]))
# print('frase[9::3] {}'.format(frase[9::3]))
# print('len(frase) {}'.format(len(frase))) # tamanho da frase
# print('frase.count("o") {}'.format(frase.count("o")))
# print('frase.count("o", 0, 13) {}'.format(frase.count("o", 0, 13)))
# print('frase.find("deo") {}'.format(frase.find("deo"))) # posição do primeira ocorrencia
# print('frase.find("android") {}'.format(frase.find("android"))) # -1 quando não encontra
# print('"Curso" in frase {}'.format("Curso" in frase)) # True ou False
# print('frase.replace("Python", "android") {}'.format(frase.replace("Python", "android")))
# print('frase.upper() {}'.format(frase.upper()))
# print('frase.lower() {}'.format(frase.lower()))
# print('frase.capitalize() {}'.format(frase.capitalize())) # apenas primeira letra da primeira palavra
# print('frase.title() {}'.format(frase.title())) # primeira letra de todas a palavras
# print('frase.strip() {}'.format(frase.strip())) # limpa espaços no inicio e final = trim
# print('frase.rstrip() {}'.format(frase.rstrip())) # limpa espaços no final
# print('frase.lstrip() {}'.format(frase.lstrip())) # limpa espaços no inico
# print('frase.split() {}'.format(frase.split())) # quebra a frase em lista
# print('"".join(frase) {}'.format("".join(frase))) # junçao de palavras e string
# frase2 = frase.split()
# frase2 = "-".join(frase2)
# print('"-".join(frase) {}'.format(frase2)) # junçao de palavras e string

elif desafio == 22:
    print('Desafio {}'.format(desafio))
    nome = str(input('Digite seu nome completo: ')).strip()
    print('Analisando o nome: {}'.format(nome))
    print('Seu nome em maiúscula é {}'.format(nome.upper()))
    print('Seu nome em minúscula é {}'.format(nome.lower()))
    print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
    nomesplit = nome.split()
    print('Seu primeiro nome é {} e ele contem {} letras'.format(nomesplit[0], len(nomesplit[0])))

elif desafio == 23:
    print('Desafio {}'.format(desafio))
    num = int(input('Digite um numero de 0 a 9999: '))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('Analisando o numero {}'.format(num))
    print('unidade: {}'.format(u))
    print('dezena: {}'.format(d))
    print('centena: {}'.format(c))
    print('milhar: {}'.format(m))

elif desafio == 24:
    print('Desafio {}'.format(desafio))
    cidade = str(input('Digite o nome de uma cidade: ')).strip()
    print('A cidade {}, começa com SANTO? {}'.format(cidade, cidade[:5].upper() == "SANTO"))

elif desafio == 25:
    print('Desafio {}'.format(desafio))
    nome = str(input('Digite um nome: '))
    print('A nome {}, contem com Silva? {}'.format(nome, "SILVA" in nome.upper()))

if desafio == 26:
    print('Desafio 026')
    frase = str(input('Diigite uma frase: ')).upper().strip()
    print('A letra "A" aparece {} vezes na frase'.format(frase.count("A")))
    print('A primeira letra "A" apareceu na posição {}'.format(frase.find("A") + 1))
    print('A ultima letra "A" apareceu na posição {}'.format(frase.rfind("A") + 1))

elif desafio == 27:
    print('Desafio {}'.format(desafio))
    nome = str(input('Digite seu nome completo: ')).strip()
    nomelista = nome.split()
    print('O primeiro nome é {}'.format(nomelista[0]))
    print('O Ultimo nome é {}'.format(nomelista[len(nomelista) - 1]))

# aula 10
elif desafio == 28:
    print('Desafio {}'.format(desafio))
    from random import randint
    from time import sleep  # faz o computador aguardar n segundos
    sorteado = randint(0, 5)  # sorteio de numeros
    print('-=-' * 20)
    print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
    print('-=-' * 20)
    jogador = int(input('Em que numero eu pensei? '))
    print('PROCESSANDO...')
    sleep(3)
    if jogador == sorteado:
        print('\033[31mPARABENS! Voce conseguiu me vencer!\033[m')
    else:
        print('\033[33mGANHEI! Eu pensei no numero {} e não no {}\033[m'.format(sorteado, jogador))

elif desafio == 29:
    print('Desafio {}'.format(desafio))
    velocidade = int(input('Qual a velocidade atual do carro? '))
    if velocidade > 80:
        print('\033[31mMULTADO! Voce excedeu o limiete permitido que é de 80Km/h\033[m')
        print('\033[31mVoce deve pagar uma multa de R${:.2f}\033[m'.format((velocidade - 80) * 7))
    print('\033[33mTenha um bom dia! Dirija com segurança!')

elif desafio == 30:
    print('Desafio {}'.format(desafio))
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        print('O numero {} é PAR'.format(num))
    else:
        print('O numero {} é IMPAR'.format(num))

elif desafio == 31:
    print('Desafio {}'.format(desafio))
    distancia = float(input('Qual a distancia da viagem em Km? '))
    print('Voce esta prestes a começar uma viagem de {}Km.'.format(distancia))
    preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45  # if na mesma linha
    print('O valor da passagem será de R${:.2f}'.format(preco))

elif desafio == 32:
    print('Desafio {}'.format(desafio))
    from datetime import date
    ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} é BISSEXTO'.format(ano))
    else:
        print('O ano {} é NÃO é BISSEXTO'.format(ano))

elif desafio == 33:
    print('Desafio {}'.format(desafio))
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    n3 = int(input('Terceiro valor: '))
    menor = n1
    if n2 < n1 and n2 < n3:
        menor = n2
    if n3 < n1 and n3 < n2:
        menor = n3
    maior = n1
    if n2 > n1 and n2 > n3:
        maior = n2
    if n3 > n1 and n3 > n2:
        maior = n3
    print('O menor valor digitado foi {}'.format(menor))
    print('O maior valor digitado foi {}'.format(maior))

elif desafio == 34:
    print('Desafio {}'.format(desafio))
    salario = float(input('Qual é o salario do funcionario? R$'))
    if salario <= 1250:
        novo = salario + (salario * 15 / 100)
    else:
        novo = salario + (salario * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

elif desafio == 35:
    print('Desafio {}'.format(desafio))
    print('\033[33m-=-' * 20)
    print('Analisador de Triangulo')
    print('\033[33m-=-' * 20)
    r1 = float(input('Primeiro segmento: '))
    r2 = float(input('Segundo segmento: '))
    r3 = float(input('Terceiro segemento: '))
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('\033[33mAs segmentos acima PODEM FORMAR um triangulo\033[m')
    else:
        print('\033[31mAs segmentos acima NÃO PODEM FORMAR um triangulo\033[m')

# aula 11
# example 033[0;33;44m
# style
# 0 = none
# 1 = bold
# 4 = underline
# 7 = negative
# text    back    colors
# 30      40      white
# 31      41      red
# 32      42      green
# 33      43      yellow
# 34      44      blue
# 35      45      purple
# 36      46      cianeto
# 37      47      gray

# aula 11
# nome = 'Leandro Weber'
# cores = {'limpa': '\033[m',
#          'azul': '\033[34m',
#          'amarelo': '\033[33m',
#          'pretoebranco': '\033[7;30m'}
# print('o nome é {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))

else:
    print('Opção inválida')
'''
opcoes = {1: opcao1, 2: opcao2, 3: opcao3, 4: opcao4, 5: opcao5, 6: opcao6, 7: opcao7, 8: opcao8, 9: opcao9,
          10: opcao10, 11: opcao11, 12: opcao12, 13: opcao13, 14: opcao14, 15: opcao15, 16: opcao16, 17: opcao17,
          18: opcao18, 19: opcao19,
          20: opcao20, 21: opcao21, 22: opcao22, 23: opcao23, 24: opcao24, 25: opcao25, 26: opcao26, 27: opcao27,
          28: opcao28, 29: opcao29,
          }
