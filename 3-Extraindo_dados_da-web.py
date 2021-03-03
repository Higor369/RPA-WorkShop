# https://rpachallengeocr.azurewebsites.net/

import rpa
import pyautogui
import pandas
import os

rpa.init()
rpa.url('https://rpachallengeocr.azurewebsites.net/')
pyautogui.sleep(6)

janela = pyautogui.getActiveWindow()
janela.maximize()

count = 1

while count <= 3:
    if count == 1:
        rpa.table('//*[@id="tableSandbox"]', 'temp.csv')
        dados = pandas.read_csv('temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=True)
        rpa.click('//*[@id="tableSandbox_next"]')
        count = count + 1
        pyautogui.sleep(1)
    else:
        rpa.table('//*[@id="tableSandbox"]', 'temp.csv')
        dados = pandas.read_csv('temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=False)
        rpa.click('//*[@id="tableSandbox_next"]')
        count = count + 1
        pyautogui.sleep(1)


janela.close()
os.remove('temp.csv')


