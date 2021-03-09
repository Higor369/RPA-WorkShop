import rpa
import pyautogui

rpa.init(visual_automation=False, chrome_browser=True)
rpa.url('https://www.melhorcambio.com/dolar-hoje')
rpa.wait(5.0)

janela = pyautogui.getActiveWindow()
janela.maximize()

rpa.type('//*[@id="original"]', '10')
pyautogui.sleep(2)

dolar_comercial = rpa.read('//*[@id="comercial"]')
pyautogui.sleep(2)

print(dolar_comercial)

janela.close()



