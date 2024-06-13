import pyautogui
import keyboard
import threading

clicking = False
click_count = 0

def rapid_click():
    global clicking
    global click_count
    clicking = True
    pyautogui.PAUSE = 0 
    while clicking and click_count < 100:
        pyautogui.click()
        click_count += 1

def stop_click():
    global clicking
    clicking = False

def start_click_thread():
    global click_count
    click_count = 0
    click_thread = threading.Thread(target=rapid_click)
    click_thread.start()

keyboard.add_hotkey('g', start_click_thread)
keyboard.add_hotkey('v', stop_click)

print("[G] Rapid clicking\n[V] Stop\n[ESC] Exit")

keyboard.wait('esc')