import pyautogui


#### Interagindo com notepad

pyautogui.hotkey('win', 'r')
pyautogui.sleep(1)
pyautogui.typewrite('notepad')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(2)

pyautogui.typewrite('Seja bem vindo ao WorkShop da FNC!')
pyautogui.sleep(2)

janela = pyautogui.getActiveWindow()
janela.close()
pyautogui.press('right')
pyautogui.sleep(2)
pyautogui.press('enter')


