import os
import time

def cls():
    os.system('cls')
def clock():
    hour = 0
    minute = 0
    seconds = 0
    timeday = 1
    day = ('am')

    while True:
        print("Time is {H}:{M}:{S} {D}".format(H=hour, M=minute, S=seconds, D=day))
        time.sleep(0.99)
        cls()
        seconds += 1

        if seconds == 60:
            minute += 1.
            seconds = 0
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            timeday += 1
            hour = 0
        if hour == 12:
            day = 'pm'
        if hour == 0:
            day = 'am'
            
if __name__ == '__main__':
    clock()
