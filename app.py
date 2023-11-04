import pyautogui
from time import sleep

pyautogui.doubleClick(32,526, duration=2)

pyautogui.click(1290,598, duration=2)

pyautogui.click(1317,544, duration=2)
pyautogui.write('Gabriell')

pyautogui.click(1300,568, duration=2)
pyautogui.write('12345')

pyautogui.click(1258,605, duration=2)

pyautogui.click(1289,540, duration=2)
pyautogui.write('Gabriell')

pyautogui.click(1273,567, duration=2)
pyautogui.write('12345')

pyautogui.click(1189,601, duration=2)

with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        pyautogui.click(1024,527, duration=2)
        pyautogui.write(produto)
        
        pyautogui.click(1023,554, duration=2)
        pyautogui.write(quantidade)
        
        pyautogui.click(1015,582, duration=2)
        pyautogui.write(preco)
        
        pyautogui.click(911,742, duration=1)