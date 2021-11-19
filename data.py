from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import monthrange


data = datetime(2021, 11, 20, 10, 50, 5)
print(data)

# formatacao de saida usastrftime
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# recebendo uma data com outro formato usa strptime
data1 = datetime.strptime('20/05/2021', '%d/%m/%Y')
print(data1)

# soma dias e segundos
data2 = data1 + timedelta(days=5, seconds=15*60*60)
print(data2)

# subtração de datas e segungos, retorna um timedelta
dif = data2 - data1
print(dif)
print(dif.days) # somente a diferença de dias
print(dif.seconds) # somente a diferença de segundos
print(dif.total_seconds()) # a diferença total representada em segundos
# print(dif.time)

# seta local conforme linhgua do pc
setlocale(LC_ALL, '') 
# setlocale(LC_ALL, 'pt_BR.utf-8') # poderia ser 

# dia e hora da execução
dt = datetime.now()
# formata: dia da semana, dia de mes de ano
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)

# utlimo dia do mes para ano bixesto
dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)