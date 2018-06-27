from threading import *
import time
def display():
    time.sleep(5)
    print("5 sec delay")

t=Thread(target = display)
t.start()

