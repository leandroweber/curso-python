dica = 'Capital de Estado'
palavras_rec = ['Maceio', 'Macapa', 'Curitiba']
palavras_des = []
palavra_des = []
cont_letras_des = 0
print('Roda a Roda Familia')

for x, palavra_rec in enumerate(palavras_rec):
    for i in range(0, len(palavra_rec)):
        palavra_des.append('_')
        cont_letras_des += 1
    palavras_des.append(palavra_des[:])
    palavra_des.clear()
for x, palavra_des in enumerate(palavras_des):
    print(f'{len(palavra_des):<2} = ', end='')
    for i in range(0, len(palavra_des)):
        print(palavra_des[i], end='')
    print()

while True:
    print(f'Dica: {dica}')
    print(f'Faltam {cont_letras_des} letras')
    letra = str(input('Digite uma letra: ')).strip().upper()[0]
    for x, palavra_rec in enumerate(palavras_rec):
        for i in range(0, len(palavra_rec)):
            if letra == palavra_rec[i].upper():
                palavras_des[x][i] = letra
                cont_letras_des -= 1
    acertou = True
    for x, palavra_des in enumerate(palavras_des):
        for i in range(0, len(palavra_des)):
            if palavra_des[i] == '_':
                acertou = False
    for x, palavra_des in enumerate(palavras_des):
        print(f'{len(palavra_des):<2} = ', end='')
        for i in range(0, len(palavra_des)):
            print(palavra_des[i], end='')
        print()
    if cont_letras_des == 0:
        break

print('Parabens')