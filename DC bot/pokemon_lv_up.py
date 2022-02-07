import pyautogui
import time
import json

time.sleep(10)
while True :
    with open("pokemon_run.json", mode="r" ) as file:
        data = json.load(file)
    if data['run'] == 't':
        pyautogui.typewrite('lll')
        pyautogui.typewrite('\n')
        time.sleep(0.7)
    else :
        time.sleep(10)