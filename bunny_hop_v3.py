import pyautogui
import keyboard
import time
import threading

clicking = False

def rapid_click():
    global clicking
    clicking = True
    while clicking:
        pyautogui.click()
        time.sleep(100) 

def stop_click():
    global clicking
    clicking = False

def start_click_thread():
    print("Starting AFK mode...")
    click_thread = threading.Thread(target=rapid_click)
    click_thread.start()

keyboard.add_hotkey('g', start_click_thread)
keyboard.add_hotkey('v', stop_click)

print("[G] Start AFK mode\n[V] Stop AFK mode\n[ESC] Exit")

keyboard.wait('esc')