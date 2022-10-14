import threading
from time import sleep

def run(content, delay=1):
    # delay in seconds
    sleep(delay)
    print(content)

thread1 = threading.Thread(target=run, args=("run 1", 3))
thread2 = threading.Thread(target=run, args=("run 2", 5))
thread1.start()
print("main Thread")
thread2.start()