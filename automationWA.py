import webbrowser
import pyautogui
import time


nama_org = input('Masukkan nama penerima pesan: ')
pesan = input('Masukkan isi pesan: ')

webbrowser.open('https://web.whatsapp.com/')

time.sleep(10)
print(pyautogui.position())

# Klik tombol new chat
pyautogui.click(168, 215)
pyautogui.typewrite(nama_org)


time.sleep(5)

# Klik nama penerima
pyautogui.click(171, 361)

time.sleep(5)

pyautogui.typewrite(pesan)

time.sleep(2)

# Klik tombol kirim
pyautogui.click(1847, 954)  
