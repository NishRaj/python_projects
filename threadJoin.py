import threading
from time import sleep

def add(delay,*args):
    sleep(delay)
    sum = 0
    for val in args:
        sum += val
    print(sum)

thread1 = threading.Thread(target=add, args=(3,1,2,3,4))
thread2 = threading.Thread(target=add, args=(1,10,11,12))
thread1.start()
thread1.join()
thread2.start()
# The active count will be 2 as thread1 will complete before we reach this line
print(threading.active_count())



