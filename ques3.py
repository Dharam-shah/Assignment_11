from threading import *
import time
def lst():
    list = [1,2,3,4,5]
    for i in range(len(list)):
        print(list[i])
        x = 2*list[i]
        time.sleep(x)

T1 = Thread(target = lst)
T1.start()