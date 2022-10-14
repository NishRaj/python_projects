import datetime
import time
from random import randint

odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]


for i in range (5):
    right_this_minute = randint(1,60)
    
    if right_this_minute in odd:
        print("There is something odd about this minute", right_this_minute)
    else:
        print("There is nothing odd about this time", right_this_minute)
    time.sleep(10) 