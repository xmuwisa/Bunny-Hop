import pyautogui
import keyboard
import threading

clicking = False
click_speed = 0.01

def rapid_click():
    global clicking
    while clicking:
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.sleep(click_speed)

def start_click():
    global clicking
    clicking = True
    click_thread = threading.Thread(target=rapid_click)
    click_thread.start()

def stop_click():
    global clicking
    clicking = False

keyboard.add_hotkey('g', start_click)
keyboard.add_hotkey('v', stop_click)

print("[G] Rapid clicking\n[V] Stop\n[ESC] Exit")

keyboard.wait('esc')