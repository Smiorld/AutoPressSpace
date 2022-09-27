import pyautogui
from pynput import keyboard

# version 1.2
def on_start_key(key):
    global startkey
    if startkey == False:
        if key != keyboard.Key.space and key != keyboard.Key.esc and key != keyboard.Key.enter and key != keyboard.Key.backspace and key != keyboard.Key.ctrl_l and key != keyboard.Key.ctrl_r and key != keyboard.Key.cmd and key != keyboard.Key.cmd_r and key != keyboard.Key.alt_l and key!= keyboard.Key.alt_gr:
            startkey=key
            print('开始键设置为',key,'，按下开始键后空格将被自动按下，手动按一次空格键即可取消。退出程序直接右上角叉掉。')
        else:
            print('开始键不能为空格，esc，ctrl，win，alt，enter，backspace,请重新设置')
    elif key == startkey :
        pyautogui.keyDown('space')

 

startkey= False
print('请按下您想要设置的本程序启动键')

with keyboard.Listener(on_press=on_start_key) as listener:
    listener.join()
