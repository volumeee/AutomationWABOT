
import webbrowser
import pyautogui
import time


nama_org = input('Masukkan nama penerima pesan: ')
pesan = input('Masukkan isi pesan: ')

webbrowser.open('https://web.whatsapp.com/')

time.sleep(10)
print(pyautogui.position())

# click on search bar
pyautogui.click(168, 215)
pyautogui.typewrite(nama_org)


time.sleep(5)

# click on person
pyautogui.click(171, 361)

time.sleep(5)

pyautogui.typewrite(pesan)

time.sleep(2)
pyautogui.click(1847, 954)  # click on Send button
