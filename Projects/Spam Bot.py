from time import sleep
import pyautogui

message = input("what the text you wanna spam: ")
n = int(input('How many times do you want to spam (-1 : infinity): '))
txt = open('spam.txt', 'w')
txt.write(message)
print("You have 10 secs to head to the message destination")
sleep(10)
if n == -1:
    while True:
        txt = open('Spam.txt')
        for l in txt:
            pyautogui.typewrite(l)
            pyautogui.press('enter')
elif n > 0:
    for i in range(n):
        txt = open('Spam.txt')
        for l in txt:
            pyautogui.typewrite(l)
            pyautogui.press('enter')
else:
    print()
