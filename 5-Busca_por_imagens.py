import rpa
import pyautogui

rpa.init()

rpa.url('https://www.google.com.br/')
pyautogui.sleep(5)

#janela = pyautogui.getActiveWindow()
#janela.maximize()

img = pyautogui.locateOnScreen('imagens/google-pesquisa.PNG', confidence='0.8')
print(img)
centro_img = pyautogui.center(img)
xposition, yposition = centro_img

pyautogui.moveTo(xposition, yposition, 2)

pyautogui.click(xposition, yposition)
pyautogui.sleep(1)

pyautogui.typewrite('fncit')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(5)

img = pyautogui.locateOnScreen('imagens/google-imagens.PNG', confidence='0.4')
print(img)
centro_img = pyautogui.center(img)
xposition, yposition = centro_img

pyautogui.moveTo(xposition, yposition, 2)
pyautogui.sleep(1)

pyautogui.click(xposition, yposition)
pyautogui.sleep(4)

img = pyautogui.locateOnScreen('imagens/fnc.PNG', confidence='0.5')
centro_img = pyautogui.center(img)
xposition, yposition = centro_img

pyautogui.click(xposition, yposition)
pyautogui.sleep(3)

pyautogui.screenshot('print.png')

#janela.close()








