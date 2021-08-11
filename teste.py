from datetime import date

# 04/07/2018

strData = '04/07/2018'

lData = strData.split('/')

strData = lData[2] + '-' + lData[1] + '-' + lData[0]


print(strData)