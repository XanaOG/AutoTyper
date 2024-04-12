import pyautogui
import sys
import time

time.sleep(3)

def type_content_with_newlines(content):
    lines = content.split('\n')
    for index, line in enumerate(lines):
        pyautogui.write(line)
        if index < len(lines) - 1:
            pyautogui.press('enter')
        time.sleep(0.05) 

args = sys.argv[1:]
if args:
    file_path = args[0]
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            type_content_with_newlines(data)
    except FileNotFoundError:
        print("Error: File not found.")
else:
    print("Please provide a file path as an argument.")
