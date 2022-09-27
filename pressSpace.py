import pyautogui
from pynput import keyboard

# version 1.0
def on_start_key(key):
    global start_key
    if key == start_key :
        pyautogui.keyDown('space')

# let the user specify the start key
while(1):
    value = input("输入数字1-5，选择本程序的启动按键：1：F1，2：F2，3：F3，4：F4，5：F5.  以回车键结束\n")
    if value == '1':
        start_key = keyboard.Key.f1
        break
    elif value == '2':
        start_key = keyboard.Key.f2
        break
    elif value == '3':  
        start_key = keyboard.Key.f3
        break
    elif value == '4':
        start_key = keyboard.Key.f4
        break
    elif value == '5':
        start_key = keyboard.Key.f5
        break
    else:
        print("输入错误，请重新输入")
    

print('设置完成，按下您设置的启动键，空格将被持续按下，手动按下并释放一次空格后停止.如需退出直接叉掉本窗口。')


with keyboard.Listener(on_press=on_start_key) as listener:
    listener.join()