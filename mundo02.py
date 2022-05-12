desafio = int(input('Escolha o desafio de 36 a 71: '))

# aula 12
# nome = str(input('Qual o seu nome? '))
# if nome == 'Leandro':
#     print('Seu nome é bem bonito')
# elif nome in 'Paulo José Maria João':
#     print('Seu nome é comum')
# else:
#     print('Seu nome é normal')
# print('Tenha um bom dia {}'.format('nome'))

if desafio == 36:
    print('Desafio {}'.format(desafio))
    imovel = float(input('Qual o valor do imovel R$'))
    salario = float(input('Qual é o seu salario R$'))
    qtdanos = int(input('Em quantos anos pretende pagar? '))
    prestacao = imovel / qtdanos / 12
    maximoapagar = salario * 30 / 100
    print(
        'Para pagar seu imóvel de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(imovel, qtdanos, prestacao))
    if prestacao <= maximoapagar:
        print('\033[33mEmpréstimo APROVADO\033[m, Sua prestação ficou abaixo de R${:.2f}'.format(maximoapagar))
    else:
        print('\033[31mEmpréstimo NEGADO\033[m, o máximo que você pode pagar é de R${:.2f}'.format(maximoapagar))


elif desafio == 37:
    print('Desafio {}'.format(desafio))
    numero = int(input('Digite um número: '))
    print('Escolha uma base de conversão:\n[1] binário\n[2] octal\n[3] hexadecimal')
    base = int(input('Qual a sua opção:'))
    if base == 1:
        print('\033[032m{}\033[m convertido em binário é igual a \033[032m{}'.format(numero, bin(numero)[2:]))
    elif base == 2:
        print('\033[032m{}\033[m convertido em octal é igual a \033[032m{}'.format(numero, oct(numero)[2:]))
    elif base == 3:
        print('\033[032m{}\033[m convertido em exadecimal é igual a \033[032m{}'.format(numero, hex(numero)[2:]))
    else:
        print('\033[031mOpção inválida.')

elif desafio == 38:
    print('Desafio {}'.format(desafio))
    num1 = int(input('Digite o PRIMEIRO número: '))
    num2 = int(input('Digite o SEGUNDO número: '))
    if num1 > num2:
        print('O \033[33mPRIMEIRO\033[m número {} é o maior'.format(num1))
    elif num2 > num1:
        print('O \033[33mSEGUNDO\033[m número {} é o maior'.format(num2))
    else:
        print('Os números {} e {} são \033[33mIGUAIS'.format(num1, num2))

elif desafio == 39:
    print('Desafio {}'.format(desafio))
    from datetime import date
    atual = date.today().year
    nascimento = int(input('Qual o ano de seu nascimento? '))
    idade = atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
    if idade == 18:
        print('\033[32mVoce tem que se alistar IMETIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('\033[33mAinda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('\033[31mVocê já deveria ter se alistado há {} anos'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))

elif desafio == 40:
    print('Desafio {}'.format(desafio))
    nota1 = float(input('Qual a sua primeira nota de 0 a 10? '))
    nota2 = float(input('Qual a sua segunda nota de 0 a 10? '))
    media = (nota1 + nota2) / 2
    print('Tirando {:.1f} e {:.1f}, a média é {:.1f}'.format(nota1, nota2, media))
    if media < 5:
        print('\33[31mVocê foi REPROVADO')
    elif media < 7:
        print('\33[33mVocê está em RECUPERAÇÃO')
    else:
        print('\33[32mVocê foi APROVADO')

elif desafio == 41:
    print('Desafio {}'.format(desafio))
    from datetime import date
    nascimento = int(input('Qual o ano de seu nascimento? '))
    idade = date.today().year - nascimento
    print('Sua idade é {} anos e você está na categoria:'.format(idade))
    if idade <= 9:
        print('Mirim')
    elif idade <= 14:
        print('Infantil')
    elif idade <= 19:
        print('Junior')
    elif idade <= 25:
        print('Senior')
    else:
        print('Master')

elif desafio == 42:
    print('Desafio {}'.format(desafio))
    r1 = float(input('Primeiro segmento: '))
    r2 = float(input('Segundo segmento: '))
    r3 = float(input('Terceiro segemento: '))
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('\033[33mAs segmentos acima PODEM FORMAR um triangulo\033[m')
        if r1 == r2 == r3:
            print('Equilátero, todos lados iguais')
        elif r1 != r2 != r3 != r1:
            print('Escaleno, todos os lados diferentes')
        else:
            print('Isóceles, dois lados iguais')
    else:
        print('\033[31mAs segmentos acima NÃO PODEM FORMAR um triangulo\033[m')

elif desafio == 43:
    print('Desafio {}'.format(desafio))
    peso = float(input('Qual o seu peso em kg '))
    altura = float(input('Qual a sua altura em m '))
    imc = peso / (altura ** 2)
    print('Seu IMC é de {:.1f}'.format(imc))
    if imc < 18.5:
        print('\33[33mAbaixo do peso')
    elif imc < 25:
        print('\33[32mPeso ideal')
    elif imc < 30:
        print('\33[33mSobrepeso')
    elif imc < 40:
        print('\33[31mObesidade')
    else:
        print('\33[35mObesidade mórbida')

elif desafio == 44:
    print('Desafio {}'.format(desafio))
    preco = float(input('Qual o preço do produto R$'))
    print('[1] À vista dinheiro/cheque: 10% desconto')
    print('[2] À vista cartão:5% desconto')
    print('[3] 2x no cartão:sem desconto')
    print('[4] 3x ou mais no cartão: 20% de juros')
    escolha = int(input('Qual a forma de pagamento:'))
    if escolha == 1:
        novo = preco - (preco * 10 / 100)
        print('O preço a vista com dinheiro ou cheque é de R${:.2f}, com 10% de desconto'.format(novo))
    elif escolha == 2:
        novo = preco - (preco * 5 / 100)
        print('O preço a vista no cartão é de R${:.2f}, com 5% de desconto'.format(novo))
    elif escolha == 3:
        parcelas = 2
        novo = preco / parcelas
        print('Em {} vezes a parcela é de R${:.2f}, sem juros'.format(parcelas, novo))
    elif escolha == 4:
        parcelas = int(input('Quantas parcelas? '))
        novo = (preco + (preco * 20 / 100)) / parcelas
        print('Em {} vezes a parcela é de R${:.2f}, com 20% de juros'.format(parcelas, novo))
    else:
        print('Opção inválida')

elif desafio == 45:
    print('Desafio {}'.format(desafio))
    from random import randint
    from time import sleep  # faz o computador aguardar n segundos
    while True:
        lista = ['Pedra', 'Papel', 'Tesoura']
        sorteado = randint(0, 2)
        print('''\033[mSuas opções:
        [0] PEDRA
        [1] PAPEL
        [2] TESOURA''')
        # print(lista[sorteado])
        jogador = int(input('Qual sua opção: '))
        if jogador > 2:
            print('Número inváldo')
        else:
            print('\033[35m', lista[0], end='  ')
            sleep(1)
            print('\033[36m', lista[1], end='  ')
            sleep(1)
            print('\033[37m', lista[2])
            sleep(1)
            print('\033[m-=-' * 15)
            print('Computador jogou {}'.format(lista[sorteado]))
            print('Jogador jogou {}'.format(lista[jogador]))
            print('-=-' * 15)
            if jogador == sorteado:
                print('\033[33mEMPATE')
            elif (jogador == 0 and sorteado == 2) or \
                    (jogador == 1 and sorteado == 0) or \
                    (jogador == 2 and sorteado == 1):
                print('\033[32mPARABENS!')
            else:
                print('\033[31mPERDEU!')
        continuar = str(input('\033[35mQuer continuar [S/N]? ')).strip().upper()[0]
        if continuar == 'N':
            break

# aula 13 for
# for c in range(0, 6):
#     print('oi')
# print('fim')
#
# for c in range(6, 0, -1):
#     print(c)
#
# for c in range(0, 7, 2):
#     print(c)
#
# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)

elif desafio == 46:
    from time import sleep
    print('Desafio {}'.format(desafio))
    print('A contagem regressiva vai começar')
    for c in range(10, -1, -1):
        print(c)
        sleep(0.5)
    print('Feliz ano novo!')

elif desafio == 47:
    print('Desafio {}'.format(desafio))
    print('Os numeros pares entre 1 e 50 são:')
    for c in range(2, 51, 2):
        print(c, end=' ')
    print('FIM')

elif desafio == 48:
    print('Desafio {}'.format(desafio))
    conta = 0
    soma = 0
    # print('Os numeros ímpares multiplos de 3 entre 1 e 500 são:')
    for c in range(1, 501, 2):
        if c % 3 == 0:
            conta += 1
            soma += c
    print('A soma dos {} números ímpares multiplos de 3 entre 1 e 500 é {}'.format(conta, soma))

elif desafio == 49:
    print('Desafio {}'.format(desafio))
    num = int(input('Digite um número '))
    print('-' * 12)
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num * c))
    print('-' * 12)

elif desafio == 50:
    print('Desafio {}'.format(desafio))
    sum = 0
    par = 0
    for c in range(1, 7):
        num = int(input('Digite um número: '))
        if num % 2 == 0:
            sum += num
            par += 1
    print('Você informou {} números PARES, e a soma é {}'.format(par, sum))

elif desafio == 51:
    print('Desafio {}'.format(desafio))
    num = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    max = num + (10 - 1) * razao
    for c in range(num, max + razao, razao):
        print('{}'.format(c), end=' -> ')
    print('FIM')

elif desafio == 52:
    print('Desafio {}'.format(desafio))
    num = int(input('Digite um número: '))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            primo = '\033[032m'
            tot += 1
        else:
            primo = '\033[31m'
        print('{}{}'.format(primo, c), end=' ')
    print('\n\033[mO número {} é divisivel {} vezes'.format(num, tot))
    if tot == 2:
        print('E por isso É PRIMO')
    else:
        print('E por isso NÃO É PRIMO')

elif desafio == 53:
    print('Desafio {}'.format(desafio))
    inverso = ''
    frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
    # for c in range(len(frase), 0, -1):
    #     inverso += frase[c-1]
    inverso = frase[::-1]
    print('Sua frase "{}" e ao contrário "{}"'.format(frase, inverso))
    if inverso == frase:
        print('É POLÍNDROMA')
    else:
        print('NÃO É POLÍNDROMA')

elif desafio == 54:
    print('Desafio {}'.format(desafio))
    from datetime import date
    atual = date.today().year
    maiores = 0
    menores = 0
    for c in range(1, 8):
        nascimento = int(input('Digite o {} ano de nascimento? '.format(c)))
        if atual - nascimento >= 21:
            maiores += 1
        else:
            menores += 1
    print('{} pessoas estão com mais de 21 anos e atingiram a maioridade'.format(maiores))
    print('{} pessoas estão com menos de 21 anos e não atingiram a maioridade'.format(menores))

elif desafio == 55:
    print('Desafio {}'.format(desafio))
    maior = 0
    menor = 0
    for c in range(1, 6):
        peso = float(input('Digite o {} peso? '.format(c)))
        if peso < menor or c == 1:
            menor = peso
        if peso > maior:
            maior = peso
    print('O Maior peso é de {}Kg'.format(maior))
    print('O menor peso é de {}Kg'.format(menor))

elif desafio == 56:
    print('Desafio {}'.format(desafio))
    media = 0
    soma = 0
    nomevelho = ''
    idadevelho = 0
    mulher20 = 0
    for c in range(1, 5):
        print('----- {} PESSOA -----'.format(c))
        nome = str(input('Nome: '.format(c))).strip()
        idade = int(input('Idade: '.format(c)))
        sexo = str(input('Sexo [M/F]: '.format(c))).upper().strip()
        soma += idade
        if sexo == 'M' and idade > idadevelho:
            idadevelho = idade
            nomevelho = nome
        if sexo == 'F' and idade < 20:
            mulher20 += 1
    media = soma / 4
    print('-' * 20)
    print('A média de idade é de {:.2f}'.format(media))
    print('O homem mais velho tem {} anos e se chama {}'.format(idadevelho, nomevelho))
    print('Tem {} mulheres com menos de 20 anos'.format(mulher20))

# aula 14 while
elif desafio == 57:
    print('Desafio {}'.format(desafio))
    sexo = str(input('Digite o sexo [M/F]:')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Dados inválidos, por favor Digite seu sexo [M/F]:')).upper().strip()[0]
    print('Sexo {} registrado com sucesso'.format(sexo))

elif desafio == 58:
    print('Desafio {} idem 28'.format(desafio))
    from random import randint
    from time import sleep  # faz o computador aguardar n segundos
    continuar = 'S'
    while continuar not in 'Nn':
        print('-=-' * 20)
        print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
        print('-=-' * 20)
        sorteado = randint(0, 10)  # sorteio de numeros
        tentativas = 0
        acertou = False
        while not acertou:
            jogador = int(input('Em que numero eu pensei? '))
            sleep(.5)
            tentativas += 1
            if jogador == sorteado:
                acertou = True
            elif jogador < sorteado:
                print('Mais...', end='')
            else:
                print('Menos...', end='')
        print('\033[33mPARABENS! Voce conseguiu me vencer com {} tentativas!\033[m'.format(tentativas))
        continuar = str(input('Quer jogar de novo [S/N]? ')).upper().strip()[0]

elif desafio == 59:
    print('Desafio {}'.format(desafio))
    from time import sleep  # faz o computador aguardar n segundos
    num1 = float(input('Digite o primeiro valor '))
    num2 = float(input('Digite o segundo valor '))
    sair = False
    while sair == False:
        print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
        opcao = int(input('>>>>>Qual a opção? '))
        if opcao == 1:
            print('A soma de {} + {} = {}'.format(num1, num2, num1 + num2))
        elif opcao == 2:
            print('O resultado de {} x {} = {}'.format(num1, num2, num1 * num2))
        elif opcao == 3:
            print('O maior número de {} e {} = '.format(num1, num2), end='')
            if num1 > num2:
                print(num1)
            elif num2 > num1:
                print(num2)
            else:
                print('São Iguais')
        elif opcao == 4:
            num1 = float(input('ReDigite o primeiro valor: '))
            num2 = float(input('ReDigite o segundo valor: '))
        elif opcao == 5:
            sair = True
            print('Finalizando...')

        else:
            print('Opção inválida')
        sleep(1)
        print('-=-' * 10)
    print('Programa encerrado!')

elif desafio == 60:
    print('Desafio {} fatorial'.format(desafio))
    # from math import fatorial
    num = int(input('Digite um numero para\nCalcular seu fatorial: '))
    # fatorial = fatorial(num)
    fatorial = 1
    # for c in range(num, 1, -1):
    c = num
    print('Calculando {}! = '.format(num), end='')
    while c > 0:
        print('{}'.format(c), end='')
        if c > 0:
            print(' x ' if c > 1 else ' = ', end='')
        fatorial *= c
        c -= 1
    print('{}'.format(fatorial))

elif desafio == 61:
    print('Desafio {} idem 51'.format(desafio))
    num = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    termo = num
    c = 1
    while c <= 10:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        c += 1
    print('FIM')

elif desafio == 62:
    print('Desafio {} idem 61'.format(desafio))
    num = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    termo = num
    c = 1
    total = 0
    mais = 10
    while mais != 0:
        total += mais
        while c <= total:
            print('{}'.format(termo), end=' -> ')
            termo += razao
            c += 1
        print('PAUSA')
        mais = int(input('Quer ver mais quantos numeros: '))
    print('Progressão finalizada mostrando {} termos'.format(total))

elif desafio == 63:
    print('Desafio {} Fibonacci'.format(desafio))
    print('Sequencia Fibonatti')
    num = int(input('Quantos termos quer mostrar? '))
    c = 3
    t1 = 0
    t2 = 1
    print('~' * 30)
    print('{} -> {}'.format(t1, t2), end='')
    while c <= num:
        t3 = t1 + t2
        print('-> {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        c += 1
    print(' -> FIM')
    print('~' * 30)

elif desafio == 64:
    print('Desafio {}'.format(desafio))
    num = conta = soma = 0
    while num != 999:
        num = int(input('Digite um numero para somar ou [999 para parar]: '))
        if num != 999:
            soma += num
            conta += 1
    print('Foram digitados {} numeros, a soma deles é {}'.format(conta, soma))

elif desafio == 65:
    print('Desafio {}'.format(desafio))
    conta = soma = maior = menor = media = 0
    resp = 'S'
    while resp in 'Ss':
        num = int(input('Digite um numero : '))
        conta += 1
        soma += num
        if conta == 1:
            maior = menor= num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    media = soma / conta
    print('Voce digitou {} números e a média foi {}'.format(conta, media))
    print('O maior é o {} e o menor o {}'.format(maior, menor))

# aula 15 while True break
# soma = 0
# while True:
#     num = int(input('Digite um numero:' ))
#     if num == 999:
#         break
#     soma += num
# nome= 'abc'
# print(f'A {nome:-^20}soma dos valores {soma}') # nova formatação

elif desafio == 66:
    print('Desafio {}'.format(desafio))
    soma = cont = 0
    while True:
        num = int(input('Digite um valor [999 para parar]: '))
        if num == 999:
            break
        soma += num
        cont += 1
    print(f'A soma dos {cont} valores foi {soma}!')

elif desafio == 67:
    print('Desafio {}'.format(desafio))
    while True:
        num = int(input('Tabuada de qual valor [negativo para parar]? '))
        c = 1
        print('-' * 30)
        if num < 0:
            break
        while c <= 10:
            print(f'{num} x {c:2} = {num*c}')
            c += 1
        print('-' * 30)
    print('Tabuada encerrrada!')

elif desafio == 68:
    print('Desafio {}'.format(desafio))
    from random import randint
    print('-=-' * 10)
    print('VAMOS JOGAR PAR OU IMPAR')
    conta = 0
    while True:
        print('-=-' * 10)
        computador = randint(1, 10)
        jogador = int(input('Diga um numero: '))
        opcao = ' '
        while opcao not in 'PI':
            opcao = str(input('Par ou Impar [P/I] ')).upper().strip()[0]
        soma = jogador + computador
        print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma} ', end='')
        if soma % 2 == 0:
            print('DEU PAR')
            if opcao == 'P':
                print('Voce VENCEU!')
                conta += 1
            else:
                print('Voce PERDEU!')
                break
        else:
            print('DEU IMPAR')
            if opcao == 'I':
                print('Voce VENCEU!')
                conta += 1
            else:
                print('Voce PERDEU!')
                break
        print('Vamos jogar novamente...')
    print('-=-' * 10)
    print(f'GAME OVER! Voce venceu {conta} vezes.')

elif desafio == 69:
    print('Desafio {}'.format(desafio))
    maior = homem = mulher = 0
    while True:
        sexo = continua = ' '
        print('-' * 20)
        print(' CADASTRO DE PESSOA')
        print('-' * 20)
        idade = int(input('Idade: '))
        while sexo not in 'MF':
            sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if idade >= 18:
            maior += 1
        if sexo == 'M':
            homem += 1
        else:
            if idade <= 20:
                mulher += 1
        print('-' * 20)
        while continua not in 'SN':
            continua = str(input('Quer Continuar [S/N] ')).upper().strip()[0]
        if continua == 'N':
            break
    print('===== FIM DO PROGRAMA =====')
    print(f'Total de pessoas com mais de 18 anos: {maior}')
    print(f'Ao todo temos {homem} homens cadastrados')
    print(f'E temos {mulher} mulheres com mais de 20 anos')

elif desafio == 70:
    print('Desafio {}'.format(desafio))
    print('-' * 20)
    print('LOJA SUPER BARATÃO')
    print('-' * 20)
    soma = qtd = barato = 0
    nomemaisbarato = ''
    while True:
        nome = str(input('Nome do Produto: '))
        preco = float(input('Preço R$ '))
        soma += preco
        if preco >= 1000:
            qtd += 1
        if nomemaisbarato == '' or preco < barato:
            nomemaisbarato = nome
            barato = preco
        continua = ' '
        while continua not in 'SN':
            continua = str(input('Quer Continuar [S/N] ')).upper().strip()[0]
        if continua in 'Nn':
            break
    print('===== FIM DO PROGRAMA =====')
    print(f'O total da compra foi R${soma}:.2f')
    print(f'Temos {qtd} produtos custando mais de R$1000.00')
    print(f'O produto mais barato foi {nomemaisbarato} que custa R${barato}:.2f')

elif desafio == 71:
    print('Desafio {}'.format(desafio))
    print('=' * 20)
    print('CAIXA ELETRONICO')
    print('Notas disponíveis: R$200, R$100, R$50, R$20, R$10, R$5, R$2, R$1')
    print('=' * 20)
    saque = 1
    #while saque % 2 != 0:
    saque = int(input('Qual o valor a sacar R$ '))
    valor = saque
    qtd = 0
    nota = 200
    while True:
        qtd = valor // nota
        # print(f'valor {valor} nota {nota} qtd {qtd}')
        if qtd > 0:
            print(f'Total de {qtd:.0f} cédulas de R${nota:.2f}')
            valor -= qtd * nota
            if valor == 0:
                break
        if nota == 200 or nota == 100 or nota == 20 or nota == 10 or nota == 2:
            nota /= 2
        elif nota == 50:
            nota = 20
        elif nota == 5:
            nota = 2
    print('=' * 20)
    print('Fim do saque!')

else:
    print('Opção inválida')

# nome = 'abc'
# print(f'A {nome:-^30} soma dos valores') # nova formatação