import pyautogui
import webbrowser
import time

message = input("apa pesan yang mau kamu spam?")
repeats = int(input("berapa kali kamu ingin mengirim pesan ini?"))
delay = int(input("berapa ms yang ingin anda tunggu di antara setiap pesan?"))

isLoaded = input("tekan enter jika discord anda sudah terbuka")


print("anda memiliki lima detik sebelum spam dimulai")

time.sleep(5)

for i in range(0, repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

    time.sleep(delay/1000)

print("Done\n")
