import pyautogui
import time

odp = input("Zapętlić ?(T/N): ")

if odp == "T":
    ile = int(input("Ile razy?: "))
    n = 1
    time.sleep(5)
    while n <= ile:
        tekst = open("tekstowy.txt", 'r')
        n = n + 1
        for word in tekst:
            pyautogui.typewrite(word)
            pyautogui.press("enter")

elif odp == "N":
    tekst = open("tekstowy.txt", 'r')
    time.sleep(5)
    for word in tekst:
        pyautogui.typewrite(word)
        pyautogui.press("enter")