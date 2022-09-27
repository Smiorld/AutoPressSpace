import pyautogui
from pynput import keyboard

# version 1.1
def on_start_key(key):
    global startkey
    if startkey == False and key != keyboard.Key.space and key != keyboard.Key.esc:
        startkey=key
        print('开始键设置为',key,'，按下开始键后空格将被自动按下，手动按一次空格键即可取消。退出程序直接右上角叉掉。')
    elif key == startkey :
        pyautogui.keyDown('space')


startkey= False
print('请按下您想要设置的本程序启动键')

with keyboard.Listener(on_press=on_start_key) as listener:
    listener.join()
