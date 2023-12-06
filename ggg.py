from pynput.keyboard import Key,Listener
import time
def on_press(key):
    if key != Key.enter:
        print(key,"------",time.time())
    else:
        print(key,"------",time.time())
        return False #按鍵不是enter,停止監視
def on_release(key):
    if key == Key.enter:
        
        pass
#監聽鍵盤按鍵
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
#停止監視
# Listener.stop()