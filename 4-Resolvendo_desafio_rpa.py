# http://www.rpachallenge.com/

import rpa
import pyautogui
import pandas
import os

rpa.init()
rpa.url('http://www.rpachallenge.com/')
pyautogui.sleep(7)

janela = pyautogui.getActiveWindow()
janela.maximize()

rpa.download('http://www.rpachallenge.com/assets/downloadFiles/challenge.xlsx', 'desafio.xlsx')
pyautogui.sleep(2)

dados = pandas.read_excel('desafio.xlsx', sheet_name='Sheet1')

colunas = ['First Name', 'Last Name ', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number']

data_frame = pandas.DataFrame(dados, columns=colunas)

for row in data_frame.itertuples():
    print(row)
    rpa.type('//*[@ng-reflect-name="labelFirstName"]', row[1])
    rpa.type('//*[@ng-reflect-name="labelLastName"]', row[2])
    rpa.type('//*[@ng-reflect-name="labelCompanyName"]', row[3])
    rpa.type('//*[@ng-reflect-name="labelRole"]', row[4])
    rpa.type('//*[@ng-reflect-name="labelAddress"]', row[5])
    rpa.type('//*[@ng-reflect-name="labelEmail"]', row[6])
    rpa.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))
    rpa.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')

os.remove('desafio.xlsx')

janela.close()



